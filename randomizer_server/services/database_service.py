import os
import random
from randomizer_server.models import Setting
from randomizer_server.serializers import SettingSerializer

def get_unique_seedID():
    seedCreated = False
    while seedCreated == False:
        random_seed_ID =  random.randint(0, 0xFFFFFFFF)
        
        try:
            Setting.objects.get(SeedID = random_seed_ID)
        except Setting.DoesNotExist:

            seedCreated = True

    return random_seed_ID


