import os
from google.cloud import storage

def save_patch_to_cloud(filename, file):
    if not os.path.isfile('service_account.json'):
        return
        
    storage_client = storage.Client.from_service_account_json('service_account.json')

    bucket = storage_client.get_bucket('paper-mario-randomizer-server.appspot.com')

    blob = storage.Blob(f'patch/{filename}', bucket)
    blob.upload_from_file(file)
