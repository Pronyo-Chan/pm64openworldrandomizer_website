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
        PartnersInDefaultLocations: bool, PartnersAlwaysUsable: bool, StartWithRandomPartners: bool, WriteSpoilerLog: bool, RandomCoinPalette: bool, RomanNumerals: bool, TurnOffMusic: bool, \
        IncludeDojo: bool, ShortenBowsersCastle: bool, ShortenCutscenes: bool = False, SkipEpilogue = False, RandomPartnersMin: int = None, RandomPartnersMax: int = None, StartWithPartners: StartWithPartners = None,
        Box5ColorA: int = 0xEBE677FF, Box5ColorB: int = 0x8E5A25FF, MarioSetting: int = 0, MarioSprite: int = 0, GoombarioSetting: int = 0, GoombarioSprite: int = 0,
        KooperSetting: int = 0, KooperSprite: int = 0, BowSetting: int = 0, BowSprite: int = 0, BossesSetting: int = 0, NPCSetting: int = 0, StartingMap: int = 0x00010104):

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
        self.RandomCoinPalette = RandomCoinPalette
        self.RomanNumerals = RomanNumerals
        self.TurnOffMusic = TurnOffMusic
        self.IncludeDojo = IncludeDojo
        self.ShortenBowsersCastle = ShortenBowsersCastle
        self.ShortenCutscenes = ShortenCutscenes
        self.SkipEpilogue = SkipEpilogue

        self.Box5ColorA = Box5ColorA
        self.Box5ColorB = Box5ColorB

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

        if StartWithRandomPartners:
            self.RandomPartnersMax = RandomPartnersMax
            self.RandomPartnersMin = RandomPartnersMin
        else:
            self.StartWithPartners = StartWithPartners

        # Other/Hidden Options
        self.SettingsName = "Default Dev Preset"
        self.SettingsVersion = "0.1"
        self.PrettySpoilerlog = True
        self.PlacementAlgorithm = "ForwardFill"
        self.PlacementLogic = "NoGlitches"

    
    