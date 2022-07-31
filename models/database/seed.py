from datetime import datetime, timedelta, timezone


class Seed:
    class StartWithPartners:
        def __init__(self, Goombario: bool, Kooper: bool, Bombette: bool, Bow: bool, Watt: bool, Sushie: bool, Lakilester: bool):
            self.Goombario = Goombario
            self.Kooper = Kooper
            self.Bombette = Bombette
            self.Bow = Bow
            self.Watt = Watt
            self.Sushie = Sushie
            self.Lakilester = Lakilester

    def __init__(self, SeedID: str, StarRodModVersion: int, AlwaysSpeedySpin: str, AlwaysISpy: bool, AlwaysPeekaboo: bool, HiddenBlockMode: int, \
        AllowPhysicsGlitches: bool, StartingCoins: int, CapEnemyXP: bool, NoXP: bool, DoubleDamage: bool, QuadrupleDamage: bool, OHKO: bool,\
        NoSaveBlocks: bool, NoHeartBlocks: bool, MagicalSeedsRequired: int, BlueHouseOpen: bool, ToyboxOpen: bool, WhaleOpen: bool, ShuffleChapterDifficulty: bool,\
        RandomFormations: bool, ShuffleItems: bool, IncludeCoins: bool, IncludeShops: bool, IncludePanels: bool, IncludeFavorsMode: int, IncludeLettersMode: int, KeyitemsOutsideDungeon: bool,\
        ProgressiveScaling: bool, RandomBadgesBP: int, RandomBadgesFP: int, RandomPartnerFP: int, RandomStarpowerSP: int, RandomQuiz: bool, SkipQuiz: bool, QuizmoAlwaysAppears: bool, \
        PartnersInDefaultLocations: bool, PartnersAlwaysUsable: bool, StartWithRandomPartners: bool, WriteSpoilerLog: bool, RomanNumerals: bool, \
        IncludeDojo: bool, BowsersCastleMode: int, ShortenCutscenes: bool = False, SkipEpilogue = False, RandomPartnersMin: int = None, RandomPartnersMax: int = None, StartWithPartners: StartWithPartners = None,
        Box5ColorA: int = 0xEBE677FF, Box5ColorB: int = 0x8E5A25FF, RandomCoinColor: bool = False, CoinColor: int = 0, MarioSetting: int = 0, MarioSprite: int = 0, GoombarioSetting: int = 0, GoombarioSprite: int = 0,
        KooperSetting: int = 0, KooperSprite: int = 0, BowSetting: int = 0, BowSprite: int = 0, BossesSetting: int = 0, NPCSetting: int = 0, EnemiesSetting: int = 0, StartingMap: int = 0x00010104,
        StartingMaxHP: int = 10, StartingMaxFP: int = 5, StartingMaxBP: int = 3, StartingStarPower: int = 0, StartingItem0: int = 0, StartingItem1: int = 0, StartingItem2: int = 0, StartingItem3: int = 0, \
        StartingItem4: int = 0, StartingItem5: int = 0, StartingItem6: int = 0, StartingItem7: int = 0, StartingItem8: int = 0, StartingItem9: int = 0, StartingItemA: int = 0, StartingItemB: int = 0, \
        StartingItemC: int = 0, StartingItemD: int = 0, StartingItemE: int = 0, ItemScarcity: int = 0, StartingItemF: int = 0, StarWaySpiritsNeeded: int = 7,  SettingsString: str = None, \
        FoliageItemHints = False, RandomText = False, NoHealingItems =  False, StartWithRandomItems: bool = False, RandomItemsMin: int = 0, RandomItemsMax: int = 0, AddItemPouches = False, \
        RandomChoice: bool = False, MysteryRandomPick: bool = False, ItemTrapMode: int = 0, AllowItemHints: bool = True, WattSetting: int = 0, WattSprite: int = 0, SushieSetting: int = 0, SushieSprite: int = 0, \
        ParakarrySetting: int = 0, ParakarrySprite: int = 0, IncludeRadioTradeEvent: bool = False, RevealLogInHours: int = 0, StartingBoots: int = 0, StartingHammer: int = 0,
        ShuffleBlocks: bool = False, RandomPitch: bool = False, BigChestShuffle: bool = False,
        PrologueGelEarly: bool = False, OddKeyEarly: bool = False, BlueHouseSkip: bool = False, BowlessToyBox: bool = False, EarlyStoreroomParakarry: bool = False, EarlyStoreroomHammer: bool = False,
        WhaleEarly: bool = False, SushielessToadTownStarPiece: bool = False, ClippyBootsStoneBlockSkip: bool = False, ClippyBootsMetalBlockSkip: bool = False, IslandPipeBlooperSkip: bool = False,
        ParakarrylessSewerStarPiece: bool = False, SewerBlocksWithoutUltraBoots: bool = False, KooperlessPleasantPathStarPiece: bool = False, InvisibleBridgeClipLzs: bool = False, InvisibleBridgeClipLaki: bool = False,
        KooperlessPleasantPathThunderBolt: bool = False, BombettelessKbfFpPlusLZS: bool = False, BombettelessKbfFpPlusLaki: bool = False, LakiJailbreak: bool = False, BombettelessRightFortressJailKey: bool = False,
        MtRuggedQuakeHammerAndLetterWithLaki: bool = False, ParakarrylessMtRuggedSeed: bool = False, BuzzarGapSkipClippy: bool = False, ParakarrylessMtRuggedStarPiece: bool = False,
        DesertBrickBlockItemWithParakarry: bool = False, EarlyRuinsLakiJump: bool = False, EarlyRuinsUltraBoots: bool = False, ArtifactJump: bool = False, RuinsKeyLakiJump: bool = False,
        ParakarylessSecondSandRoomUltraBoots: bool = False, ParakarylessSecondSandRoomNormalBoots: bool = False, ParakarylessSuperHammerRoomUltraBoots: bool = False,
        ParakarylessSuperHammerRoomNormalBoots: bool = False, RuinsLocksSkipClippy: bool = False, RecordSkipNoBombettePush: bool = False, RecordSkipBombettePush: bool = False, BoosPortraitWithKooper: bool = False,
        BoosPortraitWithLaki: bool = False, GustyGulchGateSkipLZS: bool = False, KooperlessGustyGulchDizzyDialJump: bool = False, KooperlessGustyGulchDizzyDialLaki: bool = False,
        KooperlessGustyGulchDizzyDialParakarry: bool = False, GustyGulchGapSkip: bool = False, BowlessTubbasCastle: bool = False, TubbasTableLakiJump: bool = False, TubbasCastleSuperBootsSkip: bool = False,
        ParakarrylessMegaRush: bool = False, ParakarrylessBlueBuildingStarPiece: bool = False, GourmetGuySkipJump: bool = False, GourmetGuySkipLaki: bool = False, BowlessGreenStation: bool = False,
        KooperlessRedStationShootingStar: bool = False, RaphSkipEnglish: bool = False, KooperlessLavalavaPowBlock: bool = False, UltraHammerSkip: bool = False, Flarakarry: bool = False,
        ParakarrylessFlarakarryBombette: bool = False, ParakarrylessFlarakarryLaki: bool = False, EarlyLakiLZS: bool = False, EarlyLakiBombettePush: bool = False, BombettelessMegaSmash: bool = False,
        SunTowerSkip: bool = False, YellowBerryGateSkipLZS: bool = False, YellowBerryGateSkipLaki: bool = False, YellowBerryGateSkipBombettePush: bool = False, RedBerryGateSkipBombettePush: bool = False,
        RedBerryGateSkipLaki: bool = False, BlueBerryGateSkipBombettePush: bool = False, BlueBerryGateSkipLaki: bool = False, BubbleBerryTreeLakiJump: bool = False, MurderSolvedEarlyLaki: bool = False,
        MurderSolvedEarlyBombettePush: bool = False, Ch7SushieGlitch: bool = False, ShiverMountainHiddenBlockWithoutUltraBootsLaki: bool = False, ShiverMountainHiddenBlockWithoutUltraBootsNoLaki: bool = False,
        MirrorClip: bool = False, BowlessBowsersCastleBasement: bool = False, FastFloodRoomKooper: bool = False, FastFloodRoomBombetteUltraBoots: bool = False, BreakMetalBlocksWithUltraBoots: bool = False,
        BreakYellowBlocksWithBombette: bool = False, BreakYellowBlocksWithSuperBoots: bool = False
        ):

        self.SeedID = SeedID
        self.CreationDate = datetime.now(timezone.utc)
        self.StarRodModVersion = StarRodModVersion
        self.SettingsString = SettingsString

        self.AlwaysSpeedySpin = AlwaysSpeedySpin
        self.AlwaysISpy = AlwaysISpy
        self.AlwaysPeekaboo = AlwaysPeekaboo
        self.HiddenBlockMode = HiddenBlockMode
        self.AllowPhysicsGlitches = AllowPhysicsGlitches
        self.StartingCoins = StartingCoins
        self.CapEnemyXP = CapEnemyXP
        self.NoXP = NoXP
        self.DoubleDamage = DoubleDamage
        self.QuadrupleDamage = QuadrupleDamage
        self.OHKO = OHKO
        self.NoSaveBlocks = NoSaveBlocks
        self.NoHeartBlocks = NoHeartBlocks
        self.MagicalSeedsRequired = MagicalSeedsRequired
        self.BlueHouseOpen = BlueHouseOpen
        self.ToyboxOpen = ToyboxOpen
        self.WhaleOpen = WhaleOpen
        self.ShuffleChapterDifficulty = ShuffleChapterDifficulty
        self.RandomFormations = RandomFormations 
        self.ShuffleItems = ShuffleItems
        self.IncludeCoins = IncludeCoins
        self.IncludeShops = IncludeShops
        self.IncludePanels = IncludePanels
        self.IncludeFavorsMode = IncludeFavorsMode
        self.IncludeLettersMode = IncludeLettersMode
        self.KeyitemsOutsideDungeon = KeyitemsOutsideDungeon
        self.ProgressiveScaling = ProgressiveScaling
        self.RandomBadgesBP = RandomBadgesBP
        self.RandomBadgesFP = RandomBadgesFP
        self.RandomPartnerFP = RandomPartnerFP
        self.RandomStarpowerSP = RandomStarpowerSP
        self.RandomQuiz = RandomQuiz
        self.SkipQuiz = SkipQuiz
        self.QuizmoAlwaysAppears = QuizmoAlwaysAppears
        self.PartnersInDefaultLocations = PartnersInDefaultLocations
        self.PartnersAlwaysUsable = PartnersAlwaysUsable
        self.StartWithRandomPartners = StartWithRandomPartners
        self.WriteSpoilerLog = WriteSpoilerLog
        self.RomanNumerals = RomanNumerals
        self.IncludeDojo = IncludeDojo
        self.BowsersCastleMode = BowsersCastleMode
        self.ShortenCutscenes = ShortenCutscenes
        self.SkipEpilogue = SkipEpilogue
        self.IncludeRadioTradeEvent = IncludeRadioTradeEvent

        self.Box5ColorA = Box5ColorA
        self.Box5ColorB = Box5ColorB
        self.RandomCoinColor = RandomCoinColor
        self.CoinColor = CoinColor

        self.MarioSetting = MarioSetting
        self.MarioSprite = MarioSprite
        self.GoombarioSetting = GoombarioSetting
        self.GoombarioSprite = GoombarioSprite
        self.KooperSetting = KooperSetting
        self.KooperSprite = KooperSprite
        self.BowSetting = BowSetting
        self.BowSprite = BowSprite

        self.WattSetting = WattSetting
        self.WattSprite = WattSprite
        self.SushieSetting = SushieSetting
        self.SushieSprite = SushieSprite
        self.ParakarrySetting = ParakarrySetting
        self.ParakarrySprite = ParakarrySprite

        self.BossesSetting = BossesSetting
        self.NPCSetting = NPCSetting
        self.EnemiesSetting = EnemiesSetting

        self.StartingMap = StartingMap
        self.StartingMaxHP = StartingMaxHP
        self.StartingMaxFP = StartingMaxFP
        self.StartingMaxBP = StartingMaxBP
        self.StartingLevel = int(1 + ((StartingMaxHP - 10) / 5) + ((StartingMaxFP - 5) / 5) + + ((StartingMaxBP - 3) / 3))
        self.StartingStarPower = StartingStarPower
        self.StartingBoots = StartingBoots
        self.StartingHammer = StartingHammer

        self.StartingItem0 = StartingItem0
        self.StartingItem1 = StartingItem1
        self.StartingItem2 = StartingItem2
        self.StartingItem3 = StartingItem3
        self.StartingItem4 = StartingItem4
        self.StartingItem5 = StartingItem5
        self.StartingItem6 = StartingItem6
        self.StartingItem7 = StartingItem7
        self.StartingItem8 = StartingItem8
        self.StartingItem9 = StartingItem9
        self.StartingItemA = StartingItemA
        self.StartingItemB = StartingItemB
        self.StartingItemC = StartingItemC
        self.StartingItemD = StartingItemD
        self.StartingItemE = StartingItemE
        self.StartingItemF = StartingItemF
        self.StartWithRandomItems = StartWithRandomItems
        self.RandomItemsMin = RandomItemsMin
        self.RandomItemsMax = RandomItemsMax
        self.AddItemPouches = AddItemPouches

        self.ItemScarcity = ItemScarcity
        self.StarWaySpiritsNeeded = StarWaySpiritsNeeded
        self.FoliageItemHints = FoliageItemHints
        self.RandomText = RandomText
        self.NoHealingItems = NoHealingItems

        self.RandomChoice = RandomChoice
        self.MysteryRandomPick = MysteryRandomPick
        self.ItemTrapMode = ItemTrapMode
        self.AllowItemHints = AllowItemHints
        self.ShuffleBlocks = ShuffleBlocks
        self.RandomPitch = RandomPitch
        self.BigChestShuffle = BigChestShuffle

        if StartWithRandomPartners:
            self.RandomPartnersMax = RandomPartnersMax
            self.RandomPartnersMin = RandomPartnersMin
        else:
            self.StartWithPartners = StartWithPartners

        if WriteSpoilerLog and RevealLogInHours != 0:
            self.RevealLogAtTime = datetime.now(timezone.utc) + timedelta(hours = RevealLogInHours)

        # Glitches: Goomba Region
        self.PrologueGelEarly = PrologueGelEarly

        # Glitches: Toad Town
        self.OddKeyEarly = OddKeyEarly
        self.BlueHouseSkip = BlueHouseSkip
        self.BowlessToyBox = BowlessToyBox
        self.EarlyStoreroomParakarry = EarlyStoreroomParakarry
        self.EarlyStoreroomHammer= EarlyStoreroomHammer
        self.WhaleEarly= WhaleEarly
        self.SushielessToadTownStarPiece = SushielessToadTownStarPiece

        # Glitches: Toad Town Tunnels
        self.ClippyBootsStoneBlockSkip = ClippyBootsStoneBlockSkip
        self.ClippyBootsMetalBlockSkip = ClippyBootsMetalBlockSkip
        self.IslandPipeBlooperSkip = IslandPipeBlooperSkip
        self.ParakarrylessSewerStarPiece = ParakarrylessSewerStarPiece
        self.SewerBlocksWithoutUltraBoots= SewerBlocksWithoutUltraBoots

        # Glitches: Plesant Path
        self.KooperlessPleasantPathStarPiece = KooperlessPleasantPathStarPiece
        self.InvisibleBridgeClipLzs= InvisibleBridgeClipLzs
        self.InvisibleBridgeClipLaki = InvisibleBridgeClipLaki
        self.KooperlessPleasantPathThunderBolt = KooperlessPleasantPathThunderBolt

        # Glitches: Koopa Bros Fortress
        self.BombettelessKbfFpPlusLZS= BombettelessKbfFpPlusLZS
        self.BombettelessKbfFpPlusLaki = BombettelessKbfFpPlusLaki
        self.LakiJailbreak = LakiJailbreak
        self.BombettelessRightFortressJailKey= BombettelessRightFortressJailKey

        # Glitches: Mt. Rugged
        self.MtRuggedQuakeHammerAndLetterWithLaki= MtRuggedQuakeHammerAndLetterWithLaki
        self.ParakarrylessMtRuggedSeed = ParakarrylessMtRuggedSeed
        self.BuzzarGapSkipClippy = BuzzarGapSkipClippy
        self.ParakarrylessMtRuggedStarPiece= ParakarrylessMtRuggedStarPiece

        # Glitches: Dry Dry Desert
        self.DesertBrickBlockItemWithParakarry = DesertBrickBlockItemWithParakarry
        self.EarlyRuinsLakiJump = EarlyRuinsLakiJump
        self.EarlyRuinsUltraBoots = EarlyRuinsUltraBoots

        # Glitches: Dry Dry Ruins
        self.ArtifactJump = ArtifactJump
        self.RuinsKeyLakiJump = RuinsKeyLakiJump
        self.ParakarylessSecondSandRoomUltraBoots = ParakarylessSecondSandRoomUltraBoots
        self.ParakarylessSecondSandRoomNormalBoots = ParakarylessSecondSandRoomNormalBoots
        self.ParakarylessSuperHammerRoomUltraBoots = ParakarylessSuperHammerRoomUltraBoots
        self.ParakarylessSuperHammerRoomNormalBoots = ParakarylessSuperHammerRoomNormalBoots
        self.RuinsLocksSkipClippy = RuinsLocksSkipClippy

        # Glitches: Boo's Mansion
        self.RecordSkipNoBombettePush= RecordSkipNoBombettePush
        self.RecordSkipBombettePush= RecordSkipBombettePush
        self.BoosPortraitWithKooper= BoosPortraitWithKooper
        self.BoosPortraitWithLaki= BoosPortraitWithLaki

        # Glitches: Gusty Gulch
        self.GustyGulchGateSkipLZS = GustyGulchGateSkipLZS
        self.KooperlessGustyGulchDizzyDialJump = KooperlessGustyGulchDizzyDialJump
        self.KooperlessGustyGulchDizzyDialLaki = KooperlessGustyGulchDizzyDialLaki
        self.KooperlessGustyGulchDizzyDialParakarry= KooperlessGustyGulchDizzyDialParakarry
        self.GustyGulchGapSkip = GustyGulchGapSkip

        # Glitches: Tubba's Castle
        self.BowlessTubbasCastle = BowlessTubbasCastle
        self.TubbasTableLakiJump = TubbasTableLakiJump
        self.TubbasCastleSuperBootsSkip= TubbasCastleSuperBootsSkip
        self.ParakarrylessMegaRush = ParakarrylessMegaRush

        # Glitches: Toy Box
        self.ParakarrylessBlueBuildingStarPiece= ParakarrylessBlueBuildingStarPiece
        self.GourmetGuySkipJump= GourmetGuySkipJump
        self.GourmetGuySkipLaki= GourmetGuySkipLaki
        self.BowlessGreenStation = BowlessGreenStation
        self.KooperlessRedStationShootingStar= KooperlessRedStationShootingStar

        # Glitches: Jade Jungle
        self.RaphSkipEnglish = RaphSkipEnglish

        # Glitches: Mt. Lavalava
        self.KooperlessLavalavaPowBlock = KooperlessLavalavaPowBlock
        self.UltraHammerSkip = UltraHammerSkip
        self.Flarakarry = Flarakarry
        self.ParakarrylessFlarakarryBombette = ParakarrylessFlarakarryBombette
        self.ParakarrylessFlarakarryLaki = ParakarrylessFlarakarryLaki

        # Glitches: Flower Fields
        self.EarlyLakiLZS = EarlyLakiLZS
        self.EarlyLakiBombettePush = EarlyLakiBombettePush
        self.BombettelessMegaSmash = BombettelessMegaSmash
        self.SunTowerSkip= SunTowerSkip
        self.YellowBerryGateSkipLZS = YellowBerryGateSkipLZS
        self.YellowBerryGateSkipLaki = YellowBerryGateSkipLaki
        self.YellowBerryGateSkipBombettePush = YellowBerryGateSkipBombettePush
        self.RedBerryGateSkipBombettePush = RedBerryGateSkipBombettePush
        self.RedBerryGateSkipLaki = RedBerryGateSkipLaki
        self.BlueBerryGateSkipBombettePush = BlueBerryGateSkipBombettePush
        self.BlueBerryGateSkipLaki = BlueBerryGateSkipLaki
        self.BubbleBerryTreeLakiJump = BubbleBerryTreeLakiJump

        # Glitches: Shiver Region
        self.MurderSolvedEarlyLaki = MurderSolvedEarlyLaki
        self.MurderSolvedEarlyBombettePush = MurderSolvedEarlyBombettePush
        self.Ch7SushieGlitch = Ch7SushieGlitch
        self.ShiverMountainHiddenBlockWithoutUltraBootsLaki = ShiverMountainHiddenBlockWithoutUltraBootsLaki
        self.ShiverMountainHiddenBlockWithoutUltraBootsNoLaki = ShiverMountainHiddenBlockWithoutUltraBootsNoLaki

        # Glitches: Crystal Palace
        self.MirrorClip = MirrorClip

        # Glitches: Bowser's Castle
        self.BowlessBowsersCastleBasement = BowlessBowsersCastleBasement
        self.FastFloodRoomKooper = FastFloodRoomKooper
        self.FastFloodRoomBombetteUltraBoots = FastFloodRoomBombetteUltraBoots

        # Glitches: Global
        self.BreakMetalBlocksWithUltraBoots = BreakMetalBlocksWithUltraBoots
        self.BreakYellowBlocksWithBombette = BreakYellowBlocksWithBombette
        self.BreakYellowBlocksWithSuperBoots = BreakYellowBlocksWithSuperBoots

        # Other/Hidden Options
        self.SettingsName = "Default Dev Preset"
        self.SettingsVersion = "1.0.0"
        self.PrettySpoilerlog = True
        self.PlacementAlgorithm = "AssumedFill"
        self.PlacementLogic = "NoGlitches"
        self.PeachCastleReturnPipe = True # Default
        self.ChallengeMode = False # Default

    
    
