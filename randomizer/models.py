from django.db import models


class Setting(models.Model):
    BlocksMatchContent = models.BooleanField(default=False)
    AlwaysSpeedySpin = models.BooleanField(default=False)
    AlwaysISpy = models.BooleanField(default=False)
    AlwaysPeekaboo = models.BooleanField(default=False)
    HiddenBlockMode = models.IntegerField(default=1)
    AllowPhysicsGlitches = models.BooleanField(default=False)
    InitialCoins = models.BooleanField(default=False)
    CapEnemyXP = models.BooleanField(default=False)
    NoXP = models.BooleanField(default=False)
    DoubleDamage = models.BooleanField(default=False)
    QuadrupleDamage = models.BooleanField(default=False)
    OHKO = models.BooleanField(default=False)
    NoSaveBlocks = models.BooleanField(default=False)
    NoHeartBlock = models.BooleanField(default=False)
    FlowerGateOpen = models.BooleanField(default=False)
    BlueHouseOpen = models.BooleanField(default=False)
    ToyboxOpen = models.BooleanField(default=False)
    WhaleOpen = models.BooleanField(default=False)
    ShuffleChapterDifficulty = models.BooleanField(default=False)
    RandomFormations = models.BooleanField(default=False)
    ShuffleItems = models.BooleanField(default=False)
    IncludeCoins = models.BooleanField(default=False)
    IncludeShops = models.BooleanField(default=False)
    IncludePanels = models.BooleanField(default=False)
    IncludeFavors = models.BooleanField(default=False)
    IncludeLetterChain = models.BooleanField(default=False)
    KeyitemsOutsideDungeon = models.BooleanField(default=False)
    ShuffleBadgesBP = models.BooleanField(default=False)
    ShuffleBadgesFP = models.BooleanField(default=False)
    ShufflePartnerFP = models.BooleanField(default=False)
    ShuffleStarpowerSP = models.BooleanField(default=False)
    RandomQuiz = models.BooleanField(default=False)
    SkipQuiz = models.BooleanField(default=False)
    PartnersInDefaultLocations = models.BooleanField(default=False)
    PartnersAlwaysUsable = models.BooleanField(default=False)
    StartWithRandomPartners = models.BooleanField(default=False)
    RandomPartnersMin = models.IntegerField(default=1)
    RandomPartnersMax= models.IntegerField(default=8)

    StartWithGoombario = models.BooleanField(default=True)
    StartWithKooper = models.BooleanField(default=True)
    StartWithBombette = models.BooleanField(default=True)
    StartWithBow = models.BooleanField(default=True)
    StartWithWatt = models.BooleanField(default=True)
    StartWithSushie = models.BooleanField(default=True)
    StartWithLakilester = models.BooleanField(default=True)

    WriteSpoilerLog = models.BooleanField(default=False)
    RandomCoinPalette = models.BooleanField(default=False)
    TurnOffMusic = models.BooleanField(default=False)

    # Other/Hidden Options
    IsDefault = models.BooleanField(default=False)
    SettingsName = models.CharField(max_length=100, default="Default Dev Preset")
    SettingsVersion = models.CharField(max_length=10, default="0.1")
    StartingMap = models.IntegerField(default=0x00010104)   # mac_00, Entry4
    PrettySpoilerlog = models.BooleanField(default=True)
    ColorA = models.IntegerField(default=0xEBE677FF)
    ColorB = models.IntegerField(default=0x8E5A25FF)
    
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
    PlacementAlgorithm = models.CharField(
        max_length=50,
        choices=ALGORITHM_CHOICES,
        default=FORWARD_FILL,
        null=False,
        blank=False
    )

    NO_GLITCHES = "NoGlitches"
    GLITCHES = "Glitches"
    NO_LOGIC = "NoLogic"
    LOGIC_CHOICES = [
        (NO_GLITCHES, "No Glitches"),
        (GLITCHES, "Glitches"),
        (NO_LOGIC, "No Logic"),
    ]
    PlacementLogic = models.CharField(
        max_length=50,
        choices=LOGIC_CHOICES,
        default=NO_GLITCHES,
        null=False,
        blank=False,
    )

    def __str__(self):
        return f"Setting ({self.SettingsName})"

    @property
    def StartWithPartners(self):
        return {
            "Goombario": self.StartWithGoombario,
            "Kooper": self.StartWithKooper,
            "Bombette": self.StartWithBombette,
            "Bow": self.StartWithBow,
            "Watt": self.StartWithWatt,
            "Sushie": self.StartWithSushie,
            "Lakilester": self.StartWithLakilester,
        }
