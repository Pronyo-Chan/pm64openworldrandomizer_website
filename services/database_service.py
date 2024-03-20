
import random
import services.local_storage as local_storage

def get_unique_seedID(db, collection):
    seedCreated = False
    while seedCreated == False:
        random_seed_ID =  random.randint(0, 0xFFFFFFFF)

        document =  get_document(db, collection, str(random_seed_ID))
        if document is None:
           seedCreated = True           

    return random_seed_ID

def get_document(db, collection, document_name):
    if local_storage.use_local_storage:
        return local_storage.local_seeds.get(document_name)

    document = db.collection(collection).document(str(document_name)).get()
    if not document.exists:
        return None
    
    return document.to_dict()

def set_document(db, collection, id, data):
    if local_storage.use_local_storage:
        local_storage.local_seeds[id] = data
        return

    db.collection(collection).document(id).set(data)


