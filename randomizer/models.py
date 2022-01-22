from django.db import models


DEFAULT_SETTINGS = {
   "SettingsName": "Default Dev Preset",
   "SettingsVersion": 0.1,
   "StartingMap": 0x00010104,
   "ReplaceDuplicateKeys": False,
   "DuplicateKeyReplacement": 194,
   "BlocksMatchContent": True,
   "InitialCoins": 50,
   "CapEnemyXP": True,
   "2xDamage": False,
   "4xDamage": False,
   "OHKO": False,
   "FlowerGateOpen": False,
   "BlueHouseOpen": False,
   "PlacementAlgorithm": "ForwardFill",
   "PlacementLogic": "NoGlitches",
   "ShuffleItems": True,
   "IncludeCoins": False,
   "IncludeShops": True,
   "IncludePanels": True,
   "KeyitemsOutsideArea": True,
   "KeyitemsOutsideChapter": True,
   "ShuffleEntrances": True,
   "ShuffleEntrancesByArea": True,
   "ShuffleEntrancesByAll": False,
   "MatchEntranceTypes": True,
   "RandomizeOnewayEntrances": False,
   "UnpairedEntrances": False,
   "RandomQuiz": True,
   "SkipQuiz": False,
   "StartWithRandomPartners": False,
   "RandomPartnersMin": 1,
   "RandomPartnersMax": 8,
   "StartWithGoombario": True,
   "StartWithKooper": False,
   "StartWithBombette": False,
   "StartWithParakarry": False,
   "StartWithBow": False,
   "StartWithWatt": False,
   "StartWithSushie": False,
   "StartWithLakilester": False,
   "WriteSpoilerLog": True,
   "PrettySpoilerlog": True,
   "ColorA": 0xEBE677FF,
   "ColorB": 0x8E5A25FF
}

''' Valid JSON example
{
   "seed": "ABC123",
   "SettingsName": "Default Dev Preset",
   "SettingsVersion": 0.1,
   "StartingMap": 1,
   "ReplaceDuplicateKeys": false,
   "DuplicateKeyReplacement": 194,
   "BlocksMatchContent": true,
   "InitialCoins": 50,
   "CapEnemyXP": true,
   "2xDamage": false,
   "4xDamage": false,
   "OHKO": false,
   "FlowerGateOpen": false,
   "BlueHouseOpen": false,
   "PlacementAlgorithm": "ForwardFill",
   "PlacementLogic": "NoGlitches",
   "ShuffleItems": true,
   "IncludeCoins": false,
   "IncludeShops": true,
   "IncludePanels": true,
   "KeyitemsOutsideArea": true,
   "KeyitemsOutsideChapter": true,
   "ShuffleEntrances": true,
   "ShuffleEntrancesByArea": true,
   "ShuffleEntrancesByAll": false,
   "MatchEntranceTypes": true,
   "RandomizeOnewayEntrances": false,
   "UnpairedEntrances": false,
   "RandomQuiz": true,
   "SkipQuiz": false,
   "StartWithRandomPartners": false,
   "RandomPartnersMin": 1,
   "RandomPartnersMax": 8,
   "StartWithGoombario": true,
   "StartWithKooper": false,
   "StartWithBombette": false,
   "StartWithParakarry": false,
   "StartWithBow": false,
   "StartWithWatt": false,
   "StartWithSushie": false,
   "StartWithLakilester": false,
   "WriteSpoilerLog": true,
   "PrettySpoilerlog": true,
   "ColorA": 1,
   "ColorB": 2
}
'''


class Setting(models.Model):
    default = models.BooleanField(default=False)

    name = models.CharField(max_length=50, default="Default")
    version = models.CharField(max_length=10, default="0.1")
    starting_map = models.IntegerField(default=0x00010104)

    # User Modifiable
    seed = models.CharField(max_length=32)

    replace_duplicate_keys = models.BooleanField(default=False)
    duplicate_key_replacement = models.IntegerField(default=194)

    blocks_match_content = models.BooleanField(default=True)
    initial_coins = models.IntegerField(default=50)
    cap_enemy_xp = models.BooleanField(default=True)
    damage_2x = models.BooleanField(default=False)
    damage_4x = models.BooleanField(default=False)
    one_hit_ko = models.BooleanField(default=False)

    flower_gate_open = models.BooleanField(default=False)
    blue_house_open = models.BooleanField(default=False)

    FORWARD_FILL = "ForwardFill"
    WEIGHTED_FORWARD_FILL = "WeightedForwardFill"
    ASSUMED_FILL = "AssumedFill"
    CUSTOM_SEED = "CustomSeed"
    ALGORITHM_CHOICES = [
        (FORWARD_FILL, "Forward Fill"),
        (WEIGHTED_FORWARD_FILL, "Weighted Forward Fill"),
        (ASSUMED_FILL, "Assumed Fill"),
        (CUSTOM_SEED, "Custom Seed"),
    ]

    placement_algorithm = models.CharField(
        max_length=50,
        choices=ALGORITHM_CHOICES,
        default=FORWARD_FILL,
        null=False,
        blank=False
    )

    NO_GLITCHES = "NoGlitches"
    GLITCHES = "WeightedForwardFill"
    NO_LOGIC = "AssumedFill"
    LOGIC_CHOICES = [
        (NO_GLITCHES, "No Glitches"),
        (GLITCHES, "Glitches"),
        (NO_LOGIC, "No Logic"),
    ]

    placement_logic = models.CharField(
        max_length=50,
        choices=LOGIC_CHOICES,
        default=NO_GLITCHES,
        null=False,
        blank=False,
    )

    shuffle_items = models.BooleanField(default=True)
    include_coins = models.BooleanField(default=False)
    include_shops = models.BooleanField(default=True)
    include_panels = models.BooleanField(default=True)

    key_items_outside_area = models.BooleanField(default=True)
    key_items_outside_chapter = models.BooleanField(default=True)

    shuffle_entrances = models.BooleanField(default=True)
    shuffle_entrances_by_area = models.BooleanField(default=True)
    shuffle_entrances_by_all = models.BooleanField(default=False)
    match_entrance_types = models.BooleanField(default=True)
    randomize_oneway_entrances = models.BooleanField(default=False)
    unpaired_entrances = models.BooleanField(default=False)

    random_quiz = models.BooleanField(default=True)
    skip_quiz = models.BooleanField(default=False)

    start_with_random_partners = models.BooleanField(default=False)
    random_partners_min = models.IntegerField(default=1)
    random_partners_max = models.IntegerField(default=8)

    start_with_goombario = models.BooleanField(default=True)
    start_with_kooper = models.BooleanField(default=False)
    start_with_bombette = models.BooleanField(default=False)
    start_with_parakarry = models.BooleanField(default=False)
    start_with_bow = models.BooleanField(default=False)
    start_with_watt = models.BooleanField(default=False)
    start_with_sushie = models.BooleanField(default=False)
    start_with_lakilester = models.BooleanField(default=False)

    spoiler_log = models.BooleanField(default=True)
    pretty_spoiler_log = models.BooleanField(default=True)

    color_a = models.IntegerField(default=0xEBE677FF)
    color_b = models.IntegerField(default=0x8E5A25FF)
