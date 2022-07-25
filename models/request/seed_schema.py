from marshmallow import EXCLUDE, Schema, ValidationError, fields, validates_schema, validate

CURRENT_MOD_VERSION = 7

class StartWithPartnersSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    Goombario: fields.Boolean()
    Kooper: fields.Boolean()
    Bombette: fields.Boolean()
    Bow: fields.Boolean()
    Watt: fields.Boolean()
    Sushie: fields.Boolean()
    Lakilester: fields.Boolean()

class SeedRequestSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    # Items
    ShuffleItems = fields.Boolean()
    IncludeCoins = fields.Boolean()
    IncludeShops = fields.Boolean()
    IncludePanels = fields.Boolean()
    IncludeFavorsMode = fields.Int(validate=validate.Range(0,2))
    IncludeLettersMode = fields.Int(validate=validate.Range(0,3))
    KeyitemsOutsideDungeon = fields.Boolean()
    IncludeDojo = fields.Boolean()
    AddItemPouches = fields.Boolean()
    IncludeRadioTradeEvent  = fields.Boolean()
    ShuffleBlocks = fields.Boolean()
    BigChestShuffle = fields.Boolean()
    
    # Partners
    PartnersInDefaultLocations = fields.Boolean()
    PartnersAlwaysUsable = fields.Boolean()
    StartWithRandomPartners = fields.Boolean()
    RandomPartnersMin = fields.Int(validate = validate.Range(1, 8))
    RandomPartnersMax= fields.Int(validate = validate.Range(1, 8))

    StartWithPartners = fields.Nested((StartWithPartnersSchema))

    # Gameplay
    RandomFormations = fields.Boolean()
    RandomBadgesBP = fields.Int(validate=validate.Range(0, 3))
    RandomBadgesFP = fields.Int(validate=validate.Range(0, 3))
    RandomPartnerFP = fields.Int(validate=validate.Range(0, 3))
    RandomStarpowerSP = fields.Int(validate=validate.Range(0, 3))
    RandomChoice = fields.Boolean()
    MysteryRandomPick = fields.Boolean()

    # Visuals
    RandomCoinPalette = fields.Boolean()
    RandomText = fields.Boolean()
    GoombarioSetting = fields.Int()
    GoombarioSprite= fields.Int()
    KooperSetting = fields.Int()
    KooperSprite= fields.Int()
    #BombetteSetting = fields.Int()
    #BombetteSprite= fields.Int()
    ParakarrySetting = fields.Int()
    ParakarrySprite= fields.Int()
    BowSetting = fields.Int()
    BowSprite = fields.Int()
    WattSetting = fields.Int()
    WattSprite = fields.Int()
    SushieSetting = fields.Int()
    SushieSprite = fields.Int()
    #LakilesterSetting = fields.Int()
    #LakilesterSprite = fields.Int()
    BossesSetting = fields.Int()
    NPCSetting = fields.Int()
    EnemiesSetting = fields.Int()
    MarioSetting = fields.Int()
    MarioSprite = fields.Int()
    Box5ColorA = fields.Int()
    Box5ColorB = fields.Int()
    CoinColor = fields.Int()
    RandomCoinColor = fields.Boolean()
    RandomPitch = fields.Boolean()

    # Difficulty
    StartingCoins = fields.Int(default=validate.Range(0, 999))
    CapEnemyXP = fields.Boolean()
    NoXP = fields.Boolean()
    DoubleDamage = fields.Boolean()
    QuadrupleDamage = fields.Boolean()
    OHKO = fields.Boolean()
    NoSaveBlocks = fields.Boolean()
    NoHeartBlock = fields.Boolean()
    ShuffleChapterDifficulty = fields.Boolean()
    ProgressiveScaling = fields.Boolean()
    NoHealingItems = fields.Boolean()
    NoHeartBlocks = fields.Boolean()
    ItemTrapMode = fields.Int(validate =  validate.Range(0, 3))
    ItemScarcity = fields.Int()
    AllowItemHints = fields.Boolean()
    StarWaySpiritsNeeded = fields.Int()

    # Open World
    MagicalSeedsRequired = fields.Int(validate =  validate.Range(0, 5))
    BlueHouseOpen = fields.Boolean()
    ToyboxOpen = fields.Boolean()
    WhaleOpen = fields.Boolean()
    StartingMap = fields.Int()

    # Quality of Life
    AlwaysSpeedySpin = fields.Boolean()
    AlwaysISpy = fields.Boolean()
    AlwaysPeekaboo = fields.Boolean()
    HiddenBlockMode = fields.Int(validate=validate.Range(0, 3))
    AllowPhysicsGlitches = fields.Boolean()
    RandomQuiz = fields.Boolean()
    SkipQuiz = fields.Boolean()
    QuizmoAlwaysAppears = fields.Boolean()
    RomanNumerals = fields.Boolean()
    WriteSpoilerLog = fields.Boolean()
    BowsersCastleMode = fields.Int(validate=validate.Range(0,2)) 
    FoliageItemHints = fields.Boolean()
    ShortenCutscenes = fields.Boolean()
    SkipEpilogue = fields.Boolean()

    # Starting Items
    StartWithRandomItems = fields.Boolean()
    RandomItemsMin = fields.Int(validate = validate.Range(0, 16))
    RandomItemsMax = fields.Int(validate = validate.Range(0, 16))
    StartingItem0 = fields.Int()
    StartingItem1 = fields.Int()
    StartingItem2 = fields.Int()
    StartingItem3 = fields.Int()
    StartingItem4 = fields.Int()
    StartingItem5 = fields.Int()
    StartingItem6 = fields.Int()
    StartingItem7 = fields.Int()
    StartingItem8 = fields.Int()
    StartingItem9 = fields.Int()
    StartingItemA = fields.Int()
    StartingItemB = fields.Int()
    StartingItemC = fields.Int()
    StartingItemD = fields.Int()
    StartingItemE = fields.Int()
    StartingItemF = fields.Int()

    # Starting Stats
    StartingMaxBP = fields.Int()
    StartingMaxFP = fields.Int()
    StartingMaxHP = fields.Int()
    StartingStarPower = fields.Int()
    StartingBoots = fields.Int()
    StartingHammer = fields.Int()

    #Config
    StarRodModVersion = fields.Int(validate=validate.Equal(CURRENT_MOD_VERSION))
    SettingsString = fields.String()
    RevealLogInHours = fields.Int(validate=validate.Range(0, 700))

    @validates_schema
    def validate_random_partners(self, data, **kwargs):
        if data["StartWithRandomPartners"] and data["RandomPartnersMin"] > data["RandomPartnersMax"]:
            raise ValidationError("RandomPartnersMax must be greater or equal to RandomPartnersMin")

    @validates_schema
    def validate_random_items(self, data, **kwargs):
        if data["StartWithRandomItems"] and data["RandomItemsMin"] > data["RandomItemsMax"]:
            raise ValidationError("RandomItemsMax must be greater or equal to RandomItemsMin")

