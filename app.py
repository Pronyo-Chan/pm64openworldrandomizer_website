# save this as app.py
from flask import Flask, make_response, request, abort, send_file
from flask_cors import CORS, cross_origin

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from pathlib import Path
import sys
import json

from randomizer_server.services.cloud_storage_service import get_file_from_cloud, save_file_to_cloud
from randomizer_server.services.database_service import get_unique_seedID

sys.path.insert(0, str(Path(__file__).parent / 'PMR-SeedGenerator'))
from randomizer import web_randomizer


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

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
    
@app.route('/randomizer_settings/<seed_id>', methods=['GET'])
@cross_origin()
def get_randomizer_settings(seed_id):
    if seed_id is None:
        abort(404)
    document =  db.collection(u'seeds').document(seed_id).get()
    if not document.exists:
        abort(404)
            
    return document.to_dict()

@app.route('/randomizer_settings', methods=['POST'])
@cross_origin()
def post_randomizer_settings():

    unique_seed_id = get_unique_seedID(db)
    seed_settings = request.get_json()
    seed_settings["SeedID"] = unique_seed_id

    #TODO: Add validation

    rando_settings = json.dumps(request.form.to_dict())
    rando_result = web_randomizer(unique_seed_id, rando_settings)

    db.collection(u'seeds').document(str(unique_seed_id)).set(seed_settings)

    save_file_to_cloud(str(f'patch/{unique_seed_id}.pmp'), rando_result.patchBytes)
    save_file_to_cloud(str(f'spoiler/{unique_seed_id}.txt'), rando_result.spoilerLogBytes)

    return str(unique_seed_id)

@app.route('/spoiler/<seed_id>')
@cross_origin()
def get_spoiler_log(seed_id):
    if seed_id is None:
        abort(404)
    document =  db.collection(u'seeds').document(seed_id).get()
    if not document.exists:
        abort(404)

    spoiler_file = get_file_from_cloud(f'spoiler/{seed_id}.txt')
    if spoiler_file is None:
        abort(404)

    return send_file(spoiler_file, attachment_filename="spoiler.txt")

@app.route('/patch/<seed_id>')
@cross_origin()
def get_patch(seed_id):
    if seed_id is None:
        abort(404)
    document =  db.collection(u'seeds').document(seed_id).get()
    if not document.exists:
        abort(404)

    patch_file = get_file_from_cloud(f"patch/{seed_id}.pmp")
    if patch_file is None:
        abort(404)

    return send_file(patch_file, attachment_filename="patch.pmp")