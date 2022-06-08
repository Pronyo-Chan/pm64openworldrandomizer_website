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
        NoSaveBlocks: bool, NoHeartBlocks: bool, FlowerGateOpen: bool, BlueHouseOpen: bool, ToyboxOpen: bool, WhaleOpen: bool, ShuffleChapterDifficulty: bool,\
        RandomFormations: bool, ShuffleItems: bool, IncludeCoins: bool, IncludeShops: bool, IncludePanels: bool, IncludeFavorsMode: int, IncludeLettersMode: int, KeyitemsOutsideDungeon: bool,\
        ProgressiveScaling: bool, RandomBadgesBP: int, RandomBadgesFP: int, RandomPartnerFP: int, RandomStarpowerSP: int, RandomQuiz: bool, SkipQuiz: bool, QuizmoAlwaysAppears: bool, \
        PartnersInDefaultLocations: bool, PartnersAlwaysUsable: bool, StartWithRandomPartners: bool, WriteSpoilerLog: bool, RomanNumerals: bool, \
        IncludeDojo: bool, BowsersCastleMode: int, ShortenCutscenes: bool = False, SkipEpilogue = False, RandomPartnersMin: int = None, RandomPartnersMax: int = None, StartWithPartners: StartWithPartners = None,
        Box5ColorA: int = 0xEBE677FF, Box5ColorB: int = 0x8E5A25FF, RandomCoinColor: bool = False, CoinColor: int = 0, MarioSetting: int = 0, MarioSprite: int = 0, GoombarioSetting: int = 0, GoombarioSprite: int = 0,
        KooperSetting: int = 0, KooperSprite: int = 0, BowSetting: int = 0, BowSprite: int = 0, BossesSetting: int = 0, NPCSetting: int = 0, StartingMap: int = 0x00010104,
        StartingMaxHP: int = 10, StartingMaxFP: int = 5, StartingMaxBP: int = 3, StartingStarPower: int = 0, StartingItem0: int = 0, StartingItem1: int = 0, StartingItem2: int = 0, StartingItem3: int = 0, \
        StartingItem4: int = 0, StartingItem5: int = 0, StartingItem6: int = 0, StartingItem7: int = 0, StartingItem8: int = 0, StartingItem9: int = 0, StartingItemA: int = 0, StartingItemB: int = 0, \
        StartingItemC: int = 0, StartingItemD: int = 0, StartingItemE: int = 0, ItemScarcity: int = 0, StartingItemF: int = 0, StarWaySpiritsNeeded: int = 7,  SettingsString: str = None, \
        FoliageItemHints = False, RandomText = False, NoHealingItems =  False, StartWithRandomItems: bool = False, RandomItemsMin: int = 0, RandomItemsMax: int = 0, AddItemPouches = False, \
        RandomChoice: bool = False, MysteryRandomPick: bool = False, ItemTrapMode: int = 0, AllowItemHints: bool = True, WattSetting: int = 0, WattSprite: int = 0, SushieSetting: int = 0, SushieSprite: int = 0, \
        ParakarrySetting: int = 0, ParakarrySprite: int = 0, IncludeRadioTradeEvent: bool = False, RevealLogInHours: int = 0):

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

        if StartWithRandomPartners:
            self.RandomPartnersMax = RandomPartnersMax
            self.RandomPartnersMin = RandomPartnersMin
        else:
            self.StartWithPartners = StartWithPartners

        if WriteSpoilerLog:
            self.RevealLogAtTime = datetime.now(timezone.utc) + timedelta(hours = RevealLogInHours)

        # Other/Hidden Options
        self.SettingsName = "Default Dev Preset"
        self.SettingsVersion = "1.0.0"
        self.PrettySpoilerlog = True
        self.PlacementAlgorithm = "AssumedFill"
        self.PlacementLogic = "NoGlitches"
        self.PeachCastleReturnPipe = True # Default
        self.ChallengeMode = False # Default

    
    