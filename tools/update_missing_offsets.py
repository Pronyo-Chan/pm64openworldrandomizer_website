import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Updates all the cosmetic offsets if missing. This tool can be reshaped to mass update other stuff potentially.
# Requires you to have the service_account.json DB key in the parent folder
# Usage: >python update_missing_offsets.py
def main():
    cred = credentials.Certificate('../service_account.json')
    firestore_seeds_collection = "seeds"
    
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    docs = db.collection(firestore_seeds_collection).stream()
    for doc in docs:
        seed_dict = doc.to_dict()
        seed_id = seed_dict["SeedID"]
        if not "CosmeticsOffset" in seed_dict:
            seed_dict['CosmeticsOffset'] = 30425736
            print('updated cosmetics offset for seed ' + str(seed_id))

        if not "PaletteOffset" in seed_dict:
            seed_dict['PaletteOffset'] = 30422128
            print('updated palette offset for seed ' + str(seed_id))

        if not "AudioOffset" in seed_dict:
            seed_dict['AudioOffset'] = 30425776
            print('updated audio offset for seed ' + str(seed_id))

        db.collection(firestore_seeds_collection).document(str(seed_id)).set(seed_dict)
        


if __name__ == "__main__":
    main()