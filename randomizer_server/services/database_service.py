
import random

def get_unique_seedID(db):
    seedCreated = False
    while seedCreated == False:
        random_seed_ID =  random.randint(0, 0xFFFFFFFF)

        document =  db.collection(u'seeds').document(str(random_seed_ID)).get()
        if not document.exists:
           seedCreated = True           

    return random_seed_ID


