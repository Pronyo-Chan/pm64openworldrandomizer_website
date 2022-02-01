import os
import random
from randomizer_server.models import Setting
from randomizer_server.serializers import SettingSerializer

def insert_seed_with_unique_ID(settings):
    settings_data = SettingSerializer(settings).data
    seedCreated = False
    while seedCreated == False:
        random_seed_ID =  random.randint(0, 0xFFFFFFFF)
        settings.SeedID = random_seed_ID
        
        try:
            existingSeed = Setting.objects.get(SeedID = random_seed_ID)
        except Setting.DoesNotExist:
            settings.SeedID = random_seed_ID
            settings.save()
            seedCreated = True

    return settings.SeedID


