# save this as app.py
from os import environ
from flask import Flask, make_response, request, abort, send_file
from flask_cors import CORS, cross_origin

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from pathlib import Path
import sys
import json

from marshmallow import ValidationError
from models.database.seed import Seed
from models.request.seed_schema import SeedRequestSchema
from services.cloud_storage_service import get_file_from_cloud, save_file_to_cloud
from services.database_service import get_unique_seedID

sys.path.insert(0, str(Path(__file__).parent / 'PMR-SeedGenerator'))
from randomizer import web_randomizer

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    if(environ.get("IS_PRODUCTION") == "true"):
        CORS(app, origins=["https://paper-mario-randomizer-app.ue.r.appspot.com", "https://pm64randomizer.com"])
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
environment = "uat"
if(environ.get("IS_PRODUCTION") == "true"): 
    firestore_seeds_collection = "seeds-prod"
    environment = "prod"

@app.route('/randomizer_settings/<seed_id>', methods=['GET'])
def get_randomizer_settings(seed_id):
    if seed_id is None:
        abort(404)
    document =  db.collection(firestore_seeds_collection).document(seed_id).get()
    if not document.exists:
        abort(404)
            
    return document.to_dict()

@app.route('/randomizer_settings', methods=['POST'])
def post_randomizer_settings():
    seed_dict = request.get_json()
    
    try:
        SeedRequestSchema().from_dict(seed_dict)
    except ValidationError as err:
        return err.messages, 400

    unique_seed_id = get_unique_seedID(db, firestore_seeds_collection)
    seed_dict["SeedID"] = unique_seed_id
    seed = Seed(**seed_dict)

    print(f'Request settings {seed.__dict__}')

    rando_result = web_randomizer(unique_seed_id, json.dumps(seed.__dict__, default = lambda o: f"<<non-serializable: {type(o).__qualname__}>>"))

    db.collection(firestore_seeds_collection).document(str(unique_seed_id)).set(seed.__dict__)

    save_file_to_cloud(str(f'{environment}/patch/{unique_seed_id}.pmp'), rando_result.patchBytes)
    save_file_to_cloud(str(f'{environment}/spoiler/{unique_seed_id}.txt'), rando_result.spoilerLogBytes)

    return str(unique_seed_id)

@app.route('/spoiler/<seed_id>')
def get_spoiler_log(seed_id):
    if seed_id is None:
        abort(404)
    document =  db.collection(firestore_seeds_collection).document(seed_id).get()
    if not document.exists:
        abort(404)

    spoiler_file = get_file_from_cloud(f'{environment}/spoiler/{seed_id}.txt')
    if spoiler_file is None:
        abort(404)

    return send_file(spoiler_file, attachment_filename="spoiler.txt")

@app.route('/patch/<seed_id>')
def get_patch(seed_id):
    if seed_id is None:
        abort(404)
    document =  db.collection(firestore_seeds_collection).document(seed_id).get()
    if not document.exists:
        abort(404)

    patch_file = get_file_from_cloud(f"{environment}/patch/{seed_id}.pmp")
    if patch_file is None:
        abort(404)

    return send_file(patch_file, attachment_filename="patch.pmp")