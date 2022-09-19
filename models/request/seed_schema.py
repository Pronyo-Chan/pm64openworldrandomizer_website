from marshmallow import EXCLUDE, Schema, ValidationError, fields, validates_schema, validate

CURRENT_MOD_VERSION = 8

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
    ShuffleItems = fields.Boolean(required=True)
    IncludeCoins = fields.Boolean(required=True)
    IncludeShops = fields.Boolean(required=True)
    IncludePanels = fields.Boolean(required=True)
    IncludeFavorsMode = fields.Int(required=True, validate=validate.Range(0,2))
    IncludeLettersMode = fields.Int(required=True, validate=validate.Range(0,3))
    KeyitemsOutsideDungeon = fields.Boolean(required=True)
    IncludeDojo = fields.Boolean(required=True)
    AddItemPouches = fields.Boolean(required=True)
    IncludeRadioTradeEvent  = fields.Boolean(required=True)
    ShuffleBlocks = fields.Boolean(required=True)
    GearShuffleMode = fields.Int(required=True, validate=validate.Range(0,2))
    
    # Partners
    PartnersInDefaultLocations = fields.Boolean(required=True)
    PartnersAlwaysUsable = fields.Boolean(required=True)
    StartWithRandomPartners = fields.Boolean(required=True)
    RandomPartnersMin = fields.Int(validate=validate.Range(1, 8))
    RandomPartnersMax= fields.Int(validate=validate.Range(1, 8))

    StartWithPartners = fields.Nested((StartWithPartnersSchema))

    # Gameplay
    RandomFormations = fields.Boolean(required=True)
    RandomBadgesBP = fields.Int(required=True, validate=validate.Range(0, 3))
    RandomBadgesFP = fields.Int(required=True, validate=validate.Range(0, 3))
    RandomPartnerFP = fields.Int(required=True, validate=validate.Range(0, 3))
    RandomStarpowerSP = fields.Int(required=True, validate=validate.Range(0, 3))
    RandomChoice = fields.Boolean(required=True)
    MysteryRandomPick = fields.Boolean(required=True)

    # Visuals
    RandomText = fields.Boolean(required=True)
    GoombarioSetting = fields.Int(required=True)
    GoombarioSprite= fields.Int(required=True)
    KooperSetting = fields.Int(required=True)
    KooperSprite= fields.Int(required=True)
    BombetteSetting = fields.Int(required=True)
    BombetteSprite= fields.Int(required=True)
    ParakarrySetting = fields.Int(required=True)
    ParakarrySprite= fields.Int(required=True)
    BowSetting = fields.Int(required=True)
    BowSprite = fields.Int(required=True)
    WattSetting = fields.Int(required=True)
    WattSprite = fields.Int(required=True)
    SushieSetting = fields.Int(required=True)
    SushieSprite = fields.Int(required=True)
    #LakilesterSetting = fields.Int(required=True)
    #LakilesterSprite = fields.Int(required=True)
    BossesSetting = fields.Int(required=True)
    NPCSetting = fields.Int(required=True)
    EnemiesSetting = fields.Int(required=True)
    MarioSetting = fields.Int(required=True)
    MarioSprite = fields.Int(required=True)
    Box5ColorA = fields.Int(required=True)
    Box5ColorB = fields.Int(required=True)
    CoinColor = fields.Int(required=True)
    RandomCoinColor = fields.Boolean(required=True)
    RandomPitch = fields.Boolean(required=True)

    # Difficulty
    StartingCoins = fields.Int(required=True, validate=validate.Range(0, 999))
    CapEnemyXP = fields.Boolean(required=True)
    NoXP = fields.Boolean(required=True)
    DoubleDamage = fields.Boolean(required=True)
    QuadrupleDamage = fields.Boolean(required=True)
    OHKO = fields.Boolean(required=True)
    NoSaveBlocks = fields.Boolean(required=True)
    ShuffleChapterDifficulty = fields.Boolean(required=True)
    ProgressiveScaling = fields.Boolean(required=True)
    NoHealingItems = fields.Boolean(required=True)
    NoHeartBlocks = fields.Boolean(required=True)
    ItemTrapMode = fields.Int(required=True, validate=validate.Range(0, 3))
    ItemScarcity = fields.Int(required=True)
    AllowItemHints = fields.Boolean(required=True)
    StarWaySpiritsNeeded = fields.Int(required=True)

    # Open World
    MagicalSeedsRequired = fields.Int(required=True, validate=validate.Range(0, 5))
    BlueHouseOpen = fields.Boolean(required=True)
    ToyboxOpen = fields.Boolean(required=True)
    WhaleOpen = fields.Boolean(required=True)
    StartingMap = fields.Int(required=True)

    # Quality of Life
    AlwaysSpeedySpin = fields.Boolean(required=True)
    AlwaysISpy = fields.Boolean(required=True)
    AlwaysPeekaboo = fields.Boolean(required=True)
    HiddenBlockMode = fields.Int(required=True, validate=validate.Range(0, 3))
    AllowPhysicsGlitches = fields.Boolean(required=True)
    RandomQuiz = fields.Boolean(required=True)
    SkipQuiz = fields.Boolean(required=True)
    QuizmoAlwaysAppears = fields.Boolean(required=True)
    RomanNumerals = fields.Boolean(required=True)
    WriteSpoilerLog = fields.Boolean(required=True)
    BowsersCastleMode = fields.Int(required=True, validate=validate.Range(0,2)) 
    FoliageItemHints = fields.Boolean(required=True)
    ShortenCutscenes = fields.Boolean(required=True)
    SkipEpilogue = fields.Boolean(required=True)
    HiddenPanelVisibility = fields.Int(required=True)
    CookWithoutFryingPan = fields.Boolean(required=True)
    RipCheatoItemsInLogic = fields.Int(required=True, validate=validate.Range(0, 11))

    # Starting Items
    StartWithRandomItems = fields.Boolean(required=True)
    RandomItemsMin = fields.Int(required=True, validate=validate.Range(0, 16))
    RandomItemsMax = fields.Int(required=True, validate=validate.Range(0, 16))
    StartingItem0 = fields.Int(required=True)
    StartingItem1 = fields.Int(required=True)
    StartingItem2 = fields.Int(required=True)
    StartingItem3 = fields.Int(required=True)
    StartingItem4 = fields.Int(required=True)
    StartingItem5 = fields.Int(required=True)
    StartingItem6 = fields.Int(required=True)
    StartingItem7 = fields.Int(required=True)
    StartingItem8 = fields.Int(required=True)
    StartingItem9 = fields.Int(required=True)
    StartingItemA = fields.Int(required=True)
    StartingItemB = fields.Int(required=True)
    StartingItemC = fields.Int(required=True)
    StartingItemD = fields.Int(required=True)
    StartingItemE = fields.Int(required=True)
    StartingItemF = fields.Int(required=True)

    # Starting Stats
    StartingMaxBP = fields.Int(required=True)
    StartingMaxFP = fields.Int(required=True)
    StartingMaxHP = fields.Int(required=True)
    StartingStarPower = fields.Int(required=True)
    StartingBoots = fields.Int(required=True)
    StartingHammer = fields.Int(required=True)

    # Glitches: Goomba Region
    PrologueGelEarly = fields.Boolean(required=True)
    ReverseGoombaKingBridge = fields.Boolean(required=True)
    GoombaVillageEntryFenceClip = fields.Boolean(required=True)
    GoombaVillageNpcLureExit = fields.Boolean(required=True)
    HammerlessJrPlaygroundLaki = fields.Boolean(required=True)
    GoombaVillageLakiExit = fields.Boolean(required=True)
    PrologueSushieGlitch = fields.Boolean(required=True)

    # Glitches: Toad Town
    OddKeyEarly = fields.Boolean(required=True)
    BlueHouseSkip = fields.Boolean(required=True)
    BlueHouseSkipLaki = fields.Boolean(required=True)
    BlueHouseSkipToadLure = fields.Boolean(required=True)
    BowlessToyBoxHammer = fields.Boolean(required=True)
    BowlessToyBoxHammerlessLure = fields.Boolean(required=True)
    EarlyStoreroomParakarry = fields.Boolean(required=True)
    EarlyStoreroomHammer= fields.Boolean(required=True)
    EarlyStoreroomHammerlessLure= fields.Boolean(required=True)
    WhaleEarly= fields.Boolean(required=True)
    SushielessToadTownStarPiece = fields.Boolean(required=True)
    ToadTownSushieGlitch = fields.Boolean(required=True)

    # Glitches: Toad Town Tunnels
    ClippyBootsStoneBlockSkip = fields.Boolean(required=True)
    ClippyBootsMetalBlockSkip = fields.Boolean(required=True)
    IslandPipeBlooperSkip = fields.Boolean(required=True)
    ParakarrylessSewerStarPiece = fields.Boolean(required=True)
    SewerBlocksWithoutUltraBoots= fields.Boolean(required=True)
    FirstBlockToShiverCityWithoutSuperBoots = fields.Boolean(required=True)
    BlocksToShiverCityWithKooperShellItemThrow = fields.Boolean(required=True)
    SewerYellowBlockWithUltraBoots = fields.Boolean(required=True)

    # Glitches: Plesant Path
    KooperlessPleasantPathStarPiece = fields.Boolean(required=True)
    InvisibleBridgeClipLzs= fields.Boolean(required=True)
    InvisibleBridgeClipLaki = fields.Boolean(required=True)
    KooperlessPleasantPathThunderBolt = fields.Boolean(required=True)

    # Glitches: Koopa Bros Fortress
    BombettelessKbfFpPlusLZS= fields.Boolean(required=True)
    BombettelessKbfFpPlusLaki = fields.Boolean(required=True)
    LakiJailbreak = fields.Boolean(required=True)
    BombettelessRightFortressJailKey= fields.Boolean(required=True)
    WaterStaircaseSkip= fields.Boolean(required=True)

    # Glitches: Mt. Rugged
    MtRuggedQuakeHammerAndLetterWithLaki= fields.Boolean(required=True)
    ParakarrylessMtRuggedSeed = fields.Boolean(required=True)
    BuzzarGapSkipClippy = fields.Boolean(required=True)
    ParakarrylessMtRuggedStarPiece= fields.Boolean(required=True)
    MtRuggedCoinsWithKooper= fields.Boolean(required=True)

    # Glitches: Dry Dry Desert
    DesertBrickBlockItemWithParakarry = fields.Boolean(required=True)
    EarlyRuinsLakiJump = fields.Boolean(required=True)
    EarlyRuinsUltraBoots = fields.Boolean(required=True)

    # Glitches: Dry Dry Ruins
    ArtifactJumpLaki = fields.Boolean(required=True)
    ArtifactJumpUltraBoots = fields.Boolean(required=True)
    RuinsKeyLakiJump = fields.Boolean(required=True)
    ParakarrylessSecondSandRoomUltraBoots = fields.Boolean(required=True)
    ParakarrylessSecondSandRoomNormalBoots = fields.Boolean(required=True)
    ParakarrylessSuperHammerRoomUltraBoots = fields.Boolean(required=True)
    ParakarrylessSuperHammerRoomNormalBoots = fields.Boolean(required=True)
    RuinsLocksSkipClippy = fields.Boolean(required=True)

    # Glitches: Boo's Mansion
    RecordSkipNoBombettePush= fields.Boolean(required=True)
    RecordSkipBombettePush= fields.Boolean(required=True)
    BoosPortraitWithKooper= fields.Boolean(required=True)
    BoosPortraitWithLaki= fields.Boolean(required=True)

    # Glitches: Gusty Gulch
    GustyGulchGateSkipLZS = fields.Boolean(required=True)
    GustyGulchGateSkipLaki = fields.Boolean(required=True)
    KooperlessGustyGulchDizzyDialJump = fields.Boolean(required=True)
    KooperlessGustyGulchDizzyDialLaki = fields.Boolean(required=True)
    KooperlessGustyGulchDizzyDialParakarry= fields.Boolean(required=True)
    GustyGulchGapSkip = fields.Boolean(required=True)

    # Glitches: Tubba's Castle
    BowlessTubbasCastle = fields.Boolean(required=True)
    TubbasTableLakiJump = fields.Boolean(required=True)
    TubbasTableUltraBoots = fields.Boolean(required=True)
    TubbasCastleSuperBootsSkip= fields.Boolean(required=True)
    ParakarrylessMegaRush = fields.Boolean(required=True)

    # Glitches: Toy Box
    ParakarrylessBlueBuildingStarPiece= fields.Boolean(required=True)
    GourmetGuySkipJump= fields.Boolean(required=True)
    GourmetGuySkipLaki= fields.Boolean(required=True)
    GourmetGuySkipParakarry= fields.Boolean(required=True)
    BowlessGreenStation = fields.Boolean(required=True)
    KooperlessRedStationShootingStar = fields.Boolean(required=True)
    ParakarrylessBlueBlockCityGap = fields.Boolean(required=True)
    BlueSwitchSkipLaki = fields.Boolean(required=True)
    BlueSwitchSkipUltraBoots = fields.Boolean(required=True)
    RedBarricadeSkip = fields.Boolean(required=True)
    HammerlessBlueStationLaki = fields.Boolean(required=True)
    HammerlessPinkStationLaki = fields.Boolean(required=True)

    # Glitches: Jade Jungle
    RaphSkipEnglish = fields.Boolean(required=True)
    Ch5SushieGlitch = fields.Boolean(required=True)

    # Glitches: Mt. Lavalava
    KooperlessLavalavaPowBlock = fields.Boolean(required=True)
    UltraHammerSkip = fields.Boolean(required=True)
    UltraHammerSkipLaki = fields.Boolean(required=True)
    Flarakarry = fields.Boolean(required=True)
    ParakarrylessFlarakarryBombette = fields.Boolean(required=True)
    ParakarrylessFlarakarryLaki = fields.Boolean(required=True)
    VolcanoSushieGlitch = fields.Boolean(required=True)

    # Glitches: Flower Fields
    EarlyLakiLZS = fields.Boolean(required=True)
    EarlyLakiBombettePush = fields.Boolean(required=True)
    BombettelessMegaSmash = fields.Boolean(required=True)
    SunTowerSkip= fields.Boolean(required=True)
    YellowBerryGateSkipLZS = fields.Boolean(required=True)
    YellowBerryGateSkipLaki = fields.Boolean(required=True)
    YellowBerryGateSkipBombettePush = fields.Boolean(required=True)
    RedBerryGateSkipBombettePush = fields.Boolean(required=True)
    RedBerryGateSkipLaki = fields.Boolean(required=True)
    BlueBerryGateSkipBombettePush = fields.Boolean(required=True)
    BlueBerryGateSkipLaki = fields.Boolean(required=True)
    BubbleBerryTreeLakiJump = fields.Boolean(required=True)

    # Glitches: Shiver Region
    MurderSolvedEarlyLaki = fields.Boolean(required=True)
    MurderSolvedEarlyBombettePush = fields.Boolean(required=True)
    Ch7SushieGlitch = fields.Boolean(required=True)
    StarStoneWithCh7SushieGlitch = fields.Boolean(required=True)
    ShiverMountainHiddenBlockWithoutUltraBootsLaki = fields.Boolean(required=True)
    ShiverMountainHiddenBlockWithoutUltraBootsNoLaki = fields.Boolean(required=True)
    SnowmenSkipLaki = fields.Boolean(required=True)
    ShiverMountainSwitchSkip = fields.Boolean(required=True)
    SushielessWarehouseKey = fields.Boolean(required=True)

    # Glitches: Crystal Palace
    MirrorClip = fields.Boolean(required=True)

    # Glitches: Bowser's Castle
    BowlessBowsersCastleBasement = fields.Boolean(required=True)
    BombettelessBowsersCastleBasement = fields.Boolean(required=True)
    FastFloodRoomKooper = fields.Boolean(required=True)
    FastFloodRoomBombetteUltraBoots = fields.Boolean(required=True)

    # Glitches: Global
    BreakStoneBlocksWithUltraBoots = fields.Boolean(required=True)
    BreakYellowBlocksWithSuperBoots = fields.Boolean(required=True)
    KnowsHiddenBlocks = fields.Boolean(required=True)
    KnowsPuzzleSolutions = fields.Boolean(required=True)
    ReachHighBlocksWithSuperBoots = fields.Boolean(required=True)

    #Config
    StarRodModVersion = fields.Int(required=True, validate=validate.Equal(CURRENT_MOD_VERSION))
    SettingsString = fields.String(required=True)
    RevealLogInHours = fields.Int(required=True, validate=validate.Range(0, 700))

    @validates_schema
    def validate_random_partners(self, data, **kwargs):
        if data["StartWithRandomPartners"] and data["RandomPartnersMin"] > data["RandomPartnersMax"]:
            raise ValidationError("RandomPartnersMax must be greater or equal to RandomPartnersMin")

    @validates_schema
    def validate_random_items(self, data, **kwargs):
        if data["StartWithRandomItems"] and data["RandomItemsMin"] > data["RandomItemsMax"]:
            raise ValidationError("RandomItemsMax must be greater or equal to RandomItemsMin")

