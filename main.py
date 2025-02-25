from datetime import datetime, timezone
import random
import gc
from os import environ

from flask_limiter import Limiter

from flask import Flask, request, abort, send_file, jsonify, make_response
from flask_cors import CORS
from werkzeug.exceptions import HTTPException

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
from models.request.cosmetics_schema import CosmeticsShema
from models.request.seed_schema import CURRENT_MOD_VERSION, SeedRequestSchema
from models.viewmodels.seed.seed_view_model import SeedViewModel
from services.cloud_storage_service import get_file_from_cloud, save_file_to_cloud
from services.database_service import get_unique_seedID, get_document, set_document
import services.local_storage as local_storage
from services.seed_util import build_database_seed

#from werkzeug.middleware.profiler import ProfilerMiddleware
#import memory_profiler as mem_profile

sys.path.insert(0, str(Path(__file__).parent / 'PMR-SeedGenerator'))
from randomizer import web_randomizer, web_apply_cosmetic_options
from plandomizer.plando_validator import validate_from_dict
from worldgraph import generate as generate_world_graph
from rando_modules.item_pool_too_small_error import ItemPoolTooSmallError
from rando_modules.unbeatable_plando_placement_error import UnbeatablPlandoPlacementError
from rando_modules.plando_settings_mismatch_error import PlandoSettingsMismatchError

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

    if environment != "local":
        cred = credentials.Certificate('service_account.json')
        firebase_admin.initialize_app(cred)
        global db
        db = firestore.client()

    return app

firestore_seeds_collection = "seeds"
firestore_failure_collection = "seeds-fail"
environment = "local"
db = None


if(environ.get("IS_UAT") == "true"): 
    environment = "uat"
    firestore_graphs_collection = "graphs-uat"
    local_storage.use_local_storage = False

if(environ.get("IS_PRODUCTION") == "true"): 
    firestore_seeds_collection = "seeds-prod"
    firestore_failure_collection = "seeds-fail-prod"
    firestore_graphs_collection = "graphs-prod"    
    environment = "prod"
    local_storage.use_local_storage = False

app = create_app()
limiter = Limiter(key_func=get_client_ip, app=app, storage_uri="memory://")

secret_manager = secretmanager.SecretManagerServiceClient()
api_key = secret_manager.access_secret_version(request={"name": "projects/937462171520/secrets/api-key/versions/1"}).payload.data.decode("UTF-8")

@app.errorhandler(Exception)
def handle_global_exception(e):
    print(e)
    if isinstance(e, HTTPException):
        return e
    if isinstance(e, ItemPoolTooSmallError):
        print(str(e))
        return "item_pool_too_small", 400
    if isinstance(e, UnbeatablPlandoPlacementError):
        print(str(e))
        return str(e), 400
    else:
        raise
    
@app.route('/randomizer_settings/<seed_id>', methods=['GET'])
def get_randomizer_settings(seed_id):
    if seed_id is None:
        abort(404)

    result = get_document(db, firestore_seeds_collection, seed_id)
    if result is None:
        abort(404)

    result.pop("SeedValue", None)
            
    gc.collect()
    return result

@app.route('/randomizer_settings_v2/<seed_id>', methods=['GET'])
def get_randomizer_settings_v2(seed_id):
    if seed_id is None:
        abort(404)
    
    document_dict = get_document(db, firestore_seeds_collection, seed_id)
    if document_dict is None:
        abort(404)

    result = SeedViewModel(document_dict)
            
    gc.collect()
    return result.__dict__

@app.route('/randomizer_settings', methods=['POST'])
@limiter.limit("10/hour")
def post_randomizer_settings():
    seed_request = request.get_json()
    seed_settings = seed_request.get("settings")
    plando_request = seed_request.get("plandomizer")
    
    try:
        SeedRequestSchema().load(seed_settings)
    except ValidationError as err:
        print(err)
        return err.messages, 400

    unique_seed_id = get_unique_seedID(db, firestore_seeds_collection)

    seed_settings["SeedID"] = unique_seed_id
    seed_settings["SeedValue"] = random.randint(0, 0xFFFFFFFF)
    seed_settings["CreationDate"] = datetime.now()
    
    if seed_settings.get("StarRodModVersion") is None:
        seed_settings["StarRodModVersion"] = CURRENT_MOD_VERSION

    world_graph = init_world_graph()

    print(f'Request settings {seed_request}')

    try:
        validated_plando_settings = None
        if(plando_request is not None):
            (validated_plando_settings, errors) = validate_from_dict(plando_request)
            print("validated plando settings: ", validated_plando_settings)
            print("plando errors: ", errors)
            if(len(errors.get("errors")) > 0):
                error_message = f"Invalid plandomizer config: {errors}"
                return error_message, 400
        
        rando_result = web_randomizer(
            json.dumps(seed_settings, default = lambda o: f"<<non-serializable: {type(o).__qualname__}>>"),
            validated_plando_settings,
            world_graph)
        
    except PlandoSettingsMismatchError as err:
        print(err)
        return str(err), 400
    
    except Exception as err:
        print(err)
        set_document(db, firestore_failure_collection, str(unique_seed_id), seed_settings)
        raise err

    seed_result = build_database_seed(seed_settings, plando_request is not None, rando_result)

    set_document(db, firestore_seeds_collection, str(unique_seed_id), seed_result)

    save_file_to_cloud(str(f'{environment}/patch/{unique_seed_id}.pmp'), rando_result.patchBytes)
    save_file_to_cloud(str(f'{environment}/spoiler/{unique_seed_id}.txt'), rando_result.spoilerLogBytes)

    gc.collect()
    return str(unique_seed_id)

@app.route('/randomizer_preset', methods=['POST'])
def post_randomizer_preset():
    presets = json.load(open("presets.json"))
    request_preset = request.get_json()["preset_name"]
    is_spoiler_seed = request.get_json()["spoiler_seed"]

    seed_request = next(preset["settings"] for preset in presets if request_preset == preset["name"])
    unique_seed_id = get_unique_seedID(db, firestore_seeds_collection)
    seed_request["SeedID"] = unique_seed_id
    seed_request["SeedValue"] = random.randint(0, 0xFFFFFFFF)
    
    seed_request["CreationDate"] = datetime.now()
    seed_request["StarRodModVersion"] = CURRENT_MOD_VERSION # Use latest mod version no matter what's in the preset

    if is_spoiler_seed:
        seed_request["WriteSpoilerLog"] = True
    
    world_graph = init_world_graph()

    print(f'Request settings {seed_request}')
    SeedRequestSchema().load(seed_request)

    try:
        rando_result = web_randomizer(json.dumps(seed_request, default = lambda o: f"<<non-serializable: {type(o).__qualname__}>>"), None, world_graph)
    except Exception as err:
        print(err)
        set_document(db, firestore_failure_collection, str(unique_seed_id), seed_request)
        raise err

    seed_result = build_database_seed(seed_request, False, rando_result)

    set_document(db, firestore_seeds_collection, str(unique_seed_id), seed_result)

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
    
    seed_dict = get_document(db, firestore_seeds_collection, cosmetics_dict["SeedID"])
    if seed_dict is None:
        abort(404)
    
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

    seed_dict = get_document(db, firestore_seeds_collection, str(seed_id))
    if seed_dict is None:
        abort(404)

    seed_dict["WriteSpoilerLog"] = True

    set_document(db, firestore_seeds_collection, str(seed_id), seed_dict)
    gc.collect()
    return '', 200

@app.route('/spoiler/<seed_id>', methods=['GET'])
def get_spoiler_log(seed_id):
    if seed_id is None:
        abort(404)
    seed_dict = get_document(db, firestore_seeds_collection, str(seed_id))
    if seed_dict is None:
        abort(404)

    if seed_dict["WriteSpoilerLog"] is False or ("RevealLogAtTime" in seed_dict and datetime.now(timezone.utc) < seed_dict["RevealLogAtTime"]):
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
    seed_dict = get_document(db, firestore_seeds_collection, str(seed_id))
    if seed_dict is None:
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

@app.route('/validate-plandomizer', methods=['POST'])
def post_validate_plandomizer():
    plando_request = request.get_json()
    (_, errors) = validate_from_dict(plando_request)

    return errors, 200

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
        graph_dict = get_document(db, firestore_graphs_collection, graph_name)

        if graph_dict is None:
            print("Could not find world graph version: " + graph_name + " in collection: " + firestore_graphs_collection)
            print("Generating new graph and saving to db")
            world_graph = generate_world_graph(None, None)
            dilled_graph = dill.dumps(world_graph)
            set_document(db, firestore_graphs_collection, graph_name, {'value':dilled_graph})
        else:
            db_dill_graph = graph_dict['value']
            world_graph = dill.loads(db_dill_graph)
            print("Loaded world graph version:" + graph_name + " from collection:" + firestore_graphs_collection)
    return world_graph
