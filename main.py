from datetime import datetime, timezone, timedelta
import random
import gc
from os import environ

from flask_limiter import Limiter

from flask import Flask, request, abort, send_file
from flask_cors import CORS

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud import secretmanager

from pathlib import Path
import sys
import json
import dill

from marshmallow import ValidationError
from models.database.cosmetic_settings import CosmeticSettings
from models.database.seed import Seed
from models.request.cosmetics_schema import CosmeticsShema
from models.request.seed_schema import CURRENT_MOD_VERSION, SeedRequestSchema
from models.viewmodels.seed.seed_view_model import SeedViewModel
from services.cloud_storage_service import get_file_from_cloud, save_file_to_cloud
from services.database_service import get_unique_seedID

#from werkzeug.middleware.profiler import ProfilerMiddleware
#import memory_profiler as mem_profile

sys.path.insert(0, str(Path(__file__).parent / 'PMR-SeedGenerator'))
from randomizer import web_randomizer, web_apply_cosmetic_options
from worldgraph import generate as generate_world_graph

def get_client_ip():
    if request.headers.getlist("X-Forwarded-For"):
        return request.headers.getlist("X-Forwarded-For")[0]
    else:
        return request.remote_addr

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    #app.config['PROFILE'] = True
    #app.config['DEBUG'] = True
    #app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[30])

    CORS(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    cred = credentials.Certificate('service_account.json')
    firebase_admin.initialize_app(cred)

    return app

app = create_app()
limiter = Limiter(key_func=get_client_ip, app=app, storage_uri="memory://")
db = firestore.client()

secret_manager = secretmanager.SecretManagerServiceClient()
api_key = secret_manager.access_secret_version(request={"name": "projects/937462171520/secrets/api-key/versions/1"}).payload.data.decode("UTF-8")

firestore_seeds_collection = "seeds"
firestore_failure_collection = "seeds-fail"
environment = "local"

if(environ.get("IS_UAT") == "true"): 
    environment = "uat"
    firestore_graphs_collection = "graphs-uat"

if(environ.get("IS_PRODUCTION") == "true"): 
    firestore_seeds_collection = "seeds-prod"
    firestore_failure_collection = "seeds-fail-prod"
    firestore_graphs_collection = "graphs-prod"    
    environment = "prod"

@app.route('/randomizer_settings/<seed_id>', methods=['GET'])
def get_randomizer_settings(seed_id):
    if seed_id is None:
        abort(404)
    document =  db.collection(firestore_seeds_collection).document(seed_id).get()
    if not document.exists:
        abort(404)

    result = document.to_dict()
    result.pop("SeedValue", None)
            
    gc.collect()
    return result

@app.route('/randomizer_settings_v2/<seed_id>', methods=['GET'])
def get_randomizer_settings_v2(seed_id):
    if seed_id is None:
        abort(404)
    document =  db.collection(firestore_seeds_collection).document(seed_id).get()
    if not document.exists:
        abort(404)

    document_dict = document.to_dict()
    result = SeedViewModel(document_dict)
            
    gc.collect()
    return result.__dict__

@app.route('/randomizer_settings', methods=['POST'])
@limiter.limit("10/hour")
def post_randomizer_settings():
    seed_request = request.get_json()
    
    try:
        SeedRequestSchema().load(seed_request)
    except ValidationError as err:
        print(err)
        return err.messages, 400

    unique_seed_id = get_unique_seedID(db, firestore_seeds_collection)
    seed_request["SeedID"] = unique_seed_id
    seed_request["SeedValue"] = random.randint(0, 0xFFFFFFFF)    

    world_graph = init_world_graph()

    print(f'Request settings {seed_request}')

    try:
        rando_result = web_randomizer(json.dumps(seed_request, default = lambda o: f"<<non-serializable: {type(o).__qualname__}>>"), world_graph)
    except Exception as err:
        print(err)
        db.collection(firestore_failure_collection).document(str(unique_seed_id)).set(seed_request)
        raise err

    # Transfer back the settings model data from the generator
    seed_result = rando_result.web_settings
    seed_result["PaletteOffset"] = rando_result.palette_offset
    seed_result["CosmeticsOffset"] = rando_result.cosmetics_offset
    seed_result["AudioOffset"] = rando_result.audio_offset
    seed_result["MusicOffset"] = rando_result.music_offset
    seed_result["SeedHashItems"] = rando_result.hash_items

    seed_result["SeedID"] = seed_request["SeedID"]
    seed_result["CreationDate"] = datetime.now(timezone.utc)
    seed_result["StarRodModVersion"] = seed_request["StarRodModVersion"]
    seed_result["SettingsString"] = seed_request["SettingsString"]
    if seed_request.get("WriteSpoilerLog") and seed_request.get("RevealLogInHours") != 0:
        seed_result["RevealLogAtTime"] = datetime.now(timezone.utc) + timedelta(hours = seed_request.get("RevealLogInHours"))
    seed_result["SeedValue"] = seed_request["SeedValue"]

    db.collection(firestore_seeds_collection).document(str(unique_seed_id)).set(seed_result)

    save_file_to_cloud(str(f'{environment}/patch/{unique_seed_id}.pmp'), rando_result.patchBytes)
    save_file_to_cloud(str(f'{environment}/spoiler/{unique_seed_id}.txt'), rando_result.spoilerLogBytes)

    gc.collect()
    return str(unique_seed_id)

@app.route('/randomizer_preset', methods=['POST'])
def post_randomizer_preset():
    presets = json.load(open("presets.json"))
    request_preset = request.get_json()["preset_name"]
    is_spoiler_seed = request.get_json()["spoiler_seed"]

    seed_dict = next(preset["settings"] for preset in presets if request_preset == preset["name"])
    unique_seed_id = get_unique_seedID(db, firestore_seeds_collection)
    seed_dict["SeedID"] = unique_seed_id
    
    seed_dict["CreationDate"] = datetime.now()
    seed_dict["StarRodModVersion"] = CURRENT_MOD_VERSION # Use latest mod version no matter what's in the preset

    if is_spoiler_seed:
        seed_dict["WriteSpoilerLog"] = True
    
    world_graph = init_world_graph()

    print(f'Request settings {seed_dict}')
    SeedRequestSchema().load(seed_dict)

    rando_result = web_randomizer(json.dumps(seed_dict, default = lambda o: f"<<non-serializable: {type(o).__qualname__}>>"), world_graph)
    seed_dict["SeedValue"] = rando_result.seed_value
    seed_dict["SeedHashItems"] = rando_result.hash_items
    
    seed_dict["PaletteOffset"] = rando_result.palette_offset
    seed_dict["CosmeticsOffset"] = rando_result.cosmetics_offset
    seed_dict["AudioOffset"] = rando_result.audio_offset
    seed_dict["MusicOffset"] = rando_result.music_offset


    db.collection(firestore_seeds_collection).document(str(unique_seed_id)).set(seed_dict)

    save_file_to_cloud(str(f'{environment}/patch/{unique_seed_id}.pmp'), rando_result.patchBytes)
    save_file_to_cloud(str(f'{environment}/spoiler/{unique_seed_id}.txt'), rando_result.spoilerLogBytes)

    gc.collect()
    return str(unique_seed_id)

@app.route('/cosmetics_patch', methods=['POST'])
def get_cosmetic_patch():
    cosmetics_dict = request.get_json()
    
    try:
        CosmeticsShema().load(cosmetics_dict)
    except ValidationError as err:
        print(err)
        return err.messages, 400

    if cosmetics_dict["SeedID"] is None:
        abort(404)
    document =  db.collection(firestore_seeds_collection).document(cosmetics_dict["SeedID"]).get()
    if not document.exists:
        abort(404)
    
    seed_dict = document.to_dict()
    
    cosmetic_settings = CosmeticSettings(**cosmetics_dict)

    print(f'Cosmetics Request Settings {cosmetic_settings.__dict__}')

    cosmetics_patch_operations = web_apply_cosmetic_options(cosmetic_settings.__dict__, seed_dict["PaletteOffset"], seed_dict["CosmeticsOffset"], seed_dict["AudioOffset"], seed_dict["MusicOffset"])

    gc.collect()
    return send_file(cosmetics_patch_operations, download_name="cosmetics.pmp")

@app.route('/reveal_spoiler', methods=['POST'])
def post_reveal_spoiler_log():
    request_api_key = request.get_json()["api_key"]
    seed_id = request.get_json()["seed_id"]

    if request_api_key != api_key: #This endpoint is only called by the racetime bot
        abort(400)

    document =  db.collection(firestore_seeds_collection).document(str(seed_id)).get()
    if not document.exists:
        abort(404)
    
    seed_dict = document.to_dict()

    seed_dict["WriteSpoilerLog"] = True

    db.collection(firestore_seeds_collection).document(str(seed_id)).set(seed_dict)
    gc.collect()
    return '', 200

@app.route('/spoiler/<seed_id>', methods=['GET'])
def get_spoiler_log(seed_id):
    if seed_id is None:
        abort(404)
    document =  db.collection(firestore_seeds_collection).document(seed_id).get()
    if not document.exists:
        abort(404)

    document_dict = document.to_dict()
    if document_dict["WriteSpoilerLog"] is False or ("RevealLogAtTime" in document_dict and datetime.now(timezone.utc) < document_dict["RevealLogAtTime"]):
        abort(400)

    spoiler_file = get_file_from_cloud(f'{environment}/spoiler/{seed_id}.txt')
    if spoiler_file is None:
        abort(404)

    gc.collect()
    return send_file(spoiler_file, download_name="spoiler.txt")

@app.route('/patch/<seed_id>', methods=['GET'])
def get_patch(seed_id):
    if seed_id is None:
        abort(404)
    document =  db.collection(firestore_seeds_collection).document(seed_id).get()
    if not document.exists:
        abort(404)

    patch_file = get_file_from_cloud(f"{environment}/patch/{seed_id}.pmp")
    if patch_file is None:
        abort(404)

    gc.collect()
    return send_file(patch_file, download_name="patch.pmp")

@app.route('/preset-names', methods=['GET'])
def get_preset_names():
    presets = json.load(open("presets.json"))
    preset_names =  [preset["name"] for preset in presets]
    gc.collect()
    return str(preset_names)

@app.route('/_ah/warmup')
def warmup():
    # Server stub to warmup service
    return "", 200, {}

def init_world_graph():
    if environment == "local":
        print("Running in local environment, generating world graph...")
        world_graph = generate_world_graph(None, None)
    else:

        graph_version = environ.get("GRAPH_VERSION")
        graph_name = f"world_graph_{graph_version}"
        graph_document = db.collection(firestore_graphs_collection).document(graph_name).get()

        if not graph_document.exists:
            print("Could not find world graph version: " + graph_name + " in collection: " + firestore_graphs_collection)
            print("Generating new graph and saving to db")
            world_graph = generate_world_graph(None, None)
            dilled_graph = dill.dumps(world_graph)
            db.collection(firestore_graphs_collection).document(graph_name).set({'value':dilled_graph})
        else:
            db_dill_graph = graph_document.to_dict()['value']
            world_graph = dill.loads(db_dill_graph)
            print("Loaded world graph version:" + graph_name + " from collection:" + firestore_graphs_collection)
    return world_graph
