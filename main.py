from datetime import datetime
import gc
from os import environ


from flask import Flask, make_response, request, abort, send_file
from flask_cors import CORS, cross_origin

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from pathlib import Path
import sys
import json
import dill

from marshmallow import ValidationError
from models.database.seed import Seed
from models.request.seed_schema import CURRENT_MOD_VERSION, SeedRequestSchema
from services.cloud_storage_service import get_file_from_cloud, save_file_to_cloud
from services.database_service import get_unique_seedID

#from werkzeug.middleware.profiler import ProfilerMiddleware
#import memory_profiler as mem_profile

sys.path.insert(0, str(Path(__file__).parent / 'PMR-SeedGenerator'))
from randomizer import web_randomizer
from worldgraph import generate as generate_world_graph

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    #app.config['PROFILE'] = True
    #app.config['DEBUG'] = True
    #app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[30])

    if(environ.get("IS_PRODUCTION") == "true"):
        CORS(app, origins=["https://paper-mario-randomizer-app.ue.r.appspot.com", "https://pm64randomizer.com", "https://www.pm64randomizer.com", "https://pmr-tracker.phantom-games.com"])
    else:
        CORS(app, origins=["http://localhost:4200", "https://uat-dot-paper-mario-randomizer-app.ue.r.appspot.com"])

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
db = firestore.client()

firestore_seeds_collection = "seeds"
environment = "local"

if(environ.get("IS_UAT") == "true"): 
    environment = "uat"
    firestore_graphs_collection = "graphs-uat"

if(environ.get("IS_PRODUCTION") == "true"): 
    firestore_seeds_collection = "seeds-prod"
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

@app.route('/randomizer_settings', methods=['POST'])
def post_randomizer_settings():
        
    seed_dict = request.get_json()
    
    try:
        SeedRequestSchema().load(seed_dict)
    except ValidationError as err:
        return err.messages, 400

    unique_seed_id = get_unique_seedID(db, firestore_seeds_collection)
    seed_dict["SeedID"] = unique_seed_id
    seed = Seed(**seed_dict)

    world_graph = init_world_graph(seed.BowsersCastleMode)

    print(f'Request settings {seed.__dict__}')

    rando_result = web_randomizer(json.dumps(seed.__dict__, default = lambda o: f"<<non-serializable: {type(o).__qualname__}>>"), world_graph)
    seed.SeedValue = rando_result.seed_value
    seed.PaletteOffset = rando_result.palette_offset

    db.collection(firestore_seeds_collection).document(str(unique_seed_id)).set(seed.__dict__)

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
    
    world_graph = init_world_graph(seed_dict["BowsersCastleMode"])

    print(f'Request settings {seed_dict}')

    rando_result = web_randomizer(json.dumps(seed_dict, default = lambda o: f"<<non-serializable: {type(o).__qualname__}>>"), world_graph)
    seed_dict["SeedValue"] = rando_result.seed_value

    db.collection(firestore_seeds_collection).document(str(unique_seed_id)).set(seed_dict)

    save_file_to_cloud(str(f'{environment}/patch/{unique_seed_id}.pmp'), rando_result.patchBytes)
    save_file_to_cloud(str(f'{environment}/spoiler/{unique_seed_id}.txt'), rando_result.spoilerLogBytes)

    gc.collect()
    return str(unique_seed_id)

@app.route('/spoiler/<seed_id>', methods=['GET'])
def get_spoiler_log(seed_id):
    if seed_id is None:
        abort(404)
    document =  db.collection(firestore_seeds_collection).document(seed_id).get()
    if not document.exists:
        abort(404)

    if document.to_dict()["WriteSpoilerLog"] is False:
        abort(400)

    spoiler_file = get_file_from_cloud(f'{environment}/spoiler/{seed_id}.txt')
    if spoiler_file is None:
        abort(404)

    gc.collect()
    return send_file(spoiler_file, attachment_filename="spoiler.txt")

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
    return send_file(patch_file, attachment_filename="patch.pmp")

@app.route('/preset-names', methods=['GET'])
def get_preset_names():
    presets = json.load(open("presets.json"))
    preset_names =  [preset["name"] for preset in presets]
    gc.collect()
    return str(preset_names)

def init_world_graph(bowser_castle_mode: int):
    if environment == "local":
        print("Running in local environment, generating world graph...")
        world_graph = generate_world_graph(None, None)
    else:
        graph_type = "normal"
        if bowser_castle_mode == 1:
            graph_type = "short_castle"
        elif bowser_castle_mode == 2:
            graph_type = "boss_rush_castle"

        graph_version = environ.get("GRAPH_VERSION")
        graph_name = f"{graph_type}_{graph_version}"
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