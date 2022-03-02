from datetime import datetime


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
        NoSaveBlocks: bool, NoHeartBlock: bool, FlowerGateOpen: bool, BlueHouseOpen: bool, ToyboxOpen: bool, WhaleOpen: bool, ShuffleChapterDifficulty: bool,\
        RandomFormations: bool, ShuffleItems: bool, IncludeCoins: bool, IncludeShops: bool, IncludePanels: bool, IncludeFavors: bool, IncludeLetterChain: bool, KeyitemsOutsideDungeon: bool,\
        ProgressiveScaling: bool, ShuffleBadgesBP: bool, ShuffleBadgesFP: bool, ShufflePartnerFP: bool, ShuffleStarpowerSP: bool, RandomQuiz: bool, SkipQuiz: bool, QuizmoAlwaysAppears: bool, \
        PartnersInDefaultLocations: bool, PartnersAlwaysUsable: bool, StartWithRandomPartners: bool, WriteSpoilerLog: bool, RomanNumerals: bool, TurnOffMusic: bool, \
        IncludeDojo: bool, ShortenBowsersCastle: bool, ShortenCutscenes: bool = False, SkipEpilogue = False, RandomPartnersMin: int = None, RandomPartnersMax: int = None, StartWithPartners: StartWithPartners = None,
        Box5ColorA: int = 0xEBE677FF, Box5ColorB: int = 0x8E5A25FF, RandomCoinColor: bool = False, CoinColor: int = 0, MarioSetting: int = 0, MarioSprite: int = 0, GoombarioSetting: int = 0, GoombarioSprite: int = 0,
        KooperSetting: int = 0, KooperSprite: int = 0, BowSetting: int = 0, BowSprite: int = 0, BossesSetting: int = 0, NPCSetting: int = 0, StartingMap: int = 0x00010104,
        StartingMaxHP: int = 10, StartingMaxFP: int = 5, StartingMaxBP: int = 3, StartingStarPower: int = 0, StartingItem0: int = 0, StartingItem1: int = 0, StartingItem2: int = 0, StartingItem3: int = 0, \
        StartingItem4: int = 0, StartingItem5: int = 0, StartingItem6: int = 0, StartingItem7: int = 0, StartingItem8: int = 0, StartingItem9: int = 0, StartingItemA: int = 0, StartingItemB: int = 0, \
        StartingItemC: int = 0, StartingItemD: int = 0, StartingItemE: int = 0, ItemScarcity: int = 0, StartingItemF: int = 0, StarWaySpiritsNeeded: int = 7):

        self.SeedID = SeedID
        self.CreationDate = datetime.now()
        self.StarRodModVersion = StarRodModVersion
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
        self.NoHeartBlock = NoHeartBlock
        self.FlowerGateOpen = FlowerGateOpen
        self.BlueHouseOpen = BlueHouseOpen
        self.ToyboxOpen = ToyboxOpen
        self.WhaleOpen = WhaleOpen
        self.ShuffleChapterDifficulty = ShuffleChapterDifficulty
        self.RandomFormations = RandomFormations 
        self.ShuffleItems = ShuffleItems
        self.IncludeCoins = IncludeCoins
        self.IncludeShops = IncludeShops
        self.IncludePanels = IncludePanels
        self.IncludeFavors = IncludeFavors
        self.IncludeLetterChain = IncludeLetterChain
        self.KeyitemsOutsideDungeon = KeyitemsOutsideDungeon
        self.ProgressiveScaling = ProgressiveScaling
        self.ShuffleBadgesBP = ShuffleBadgesBP
        self.ShuffleBadgesFP = ShuffleBadgesFP
        self.ShufflePartnerFP = ShufflePartnerFP
        self.ShuffleStarpowerSP = ShuffleStarpowerSP
        self.RandomQuiz = RandomQuiz
        self.SkipQuiz = SkipQuiz
        self.QuizmoAlwaysAppears = QuizmoAlwaysAppears
        self.PartnersInDefaultLocations = PartnersInDefaultLocations
        self.PartnersAlwaysUsable = PartnersAlwaysUsable
        self.StartWithRandomPartners = StartWithRandomPartners
        self.WriteSpoilerLog = WriteSpoilerLog
        self.RomanNumerals = RomanNumerals
        self.TurnOffMusic = TurnOffMusic
        self.IncludeDojo = IncludeDojo
        self.ShortenBowsersCastle = ShortenBowsersCastle
        self.ShortenCutscenes = ShortenCutscenes
        self.SkipEpilogue = SkipEpilogue

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

        self.BossesSetting = BossesSetting
        self.NPCSetting = NPCSetting

        
        self.StartingMap = StartingMap
        self.StartingMaxHP = StartingMaxHP
        self.StartingMaxFP = StartingMaxFP
        self.StartingMaxBP = StartingMaxBP
        self.StartingLevel = int(1 + ((StartingMaxHP - 10) / 5) + ((StartingMaxFP - 5) / 5) + + ((StartingMaxBP - 3) / 3))
        self.StartingStarPower = StartingStarPower

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

        self.ItemScarcity = ItemScarcity
        self.StarWaySpiritsNeeded = StarWaySpiritsNeeded

        if StartWithRandomPartners:
            self.RandomPartnersMax = RandomPartnersMax
            self.RandomPartnersMin = RandomPartnersMin
        else:
            self.StartWithPartners = StartWithPartners

        # Other/Hidden Options
        self.SettingsName = "Default Dev Preset"
        self.SettingsVersion = "1.0.0"
        self.PrettySpoilerlog = True
        self.PlacementAlgorithm = "ForwardFill"
        self.PlacementLogic = "NoGlitches"
        self.PeachCastleReturnPipe = True # Default

    
    