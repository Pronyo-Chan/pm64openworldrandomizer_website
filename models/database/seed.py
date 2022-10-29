from datetime import datetime, timedelta, timezone
from services.seed_hash_service import get_items_from_seed_id


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
        IncludeDojo: bool, BowsersCastleMode: int, ShortenCutscenes: bool, SkipEpilogue, RandomPartnersMin: int, RandomPartnersMax: int, StartWithPartners: StartWithPartners,
        Box5ColorA: int, Box5ColorB: int, RandomCoinColor: bool, CoinColor: int, MarioSetting: int, MarioSprite: int, GoombarioSetting: int, GoombarioSprite: int,
        KooperSetting: int, KooperSprite: int, BowSetting: int, BowSprite: int, BossesSetting: int, NPCSetting: int, EnemiesSetting: int, StartingMap: int,
        StartingMaxHP: int, StartingMaxFP: int, StartingMaxBP: int, StartingStarPower: int, StartingItem0: int, StartingItem1: int, StartingItem2: int, StartingItem3: int, \
        StartingItem4: int, StartingItem5: int, StartingItem6: int, StartingItem7: int, StartingItem8: int, StartingItem9: int, StartingItemA: int, StartingItemB: int, \
        StartingItemC: int, StartingItemD: int, StartingItemE: int, RandomConsumableMode: int, ItemQuality: int, StartingItemF: int, StarWaySpiritsNeeded: int,  SettingsString: str, \
        FoliageItemHints, RandomText, NoHealingItems, StartWithRandomItems: bool, RandomItemsMin: int, RandomItemsMax: int, AddItemPouches, \
        RandomChoice: bool, MysteryRandomPick: bool, ItemTrapMode: int, AllowItemHints: bool, WattSetting: int, WattSprite: int, SushieSetting: int, SushieSprite: int, \
        ParakarrySetting: int, ParakarrySprite: int, IncludeRadioTradeEvent: bool, RevealLogInHours: int, StartingBoots: int, StartingHammer: int,
        ShuffleBlocks: bool, RandomPitch: bool, GearShuffleMode: int, HiddenPanelVisibility: bool, BombetteSetting: int, BombetteSprite: int, CookWithoutFryingPan: bool,
        RipCheatoItemsInLogic: int, MerlowRewardPricing: int, PrologueOpen: bool,

        PrologueGelEarly: bool, ReverseGoombaKingBridge: bool, GoombaVillageEntryFenceClip: bool, GoombaVillageNpcLureExit: bool, HammerlessJrPlaygroundLaki: bool, GoombaVillageLakiExit: bool,
        PrologueSushieGlitchKsj: bool, PrologueSushieGlitchUltraBootsLaki: bool, OddKeyEarly: bool, BlueHouseSkip: bool, BlueHouseSkipLaki: bool, BlueHouseSkipToadLure: bool, BowlessToyBoxHammer: bool, BowlessToyBoxHammerlessLure: bool,
        EarlyStoreroomParakarry: bool, EarlyStoreroomHammer: bool, EarlyStoreroomHammerlessLure: bool, WhaleEarly: bool, SushielessToadTownStarPiece: bool, ClippyBootsStoneBlockSkip: bool,
        ToadTownSushieGlitch: bool, ClippyBootsMetalBlockSkip: bool, IslandPipeBlooperSkip: bool, ParakarrylessSewerStarPiece: bool, SewerBlocksWithoutUltraBoots: bool,
        FirstBlockToShiverCityWithoutSuperBoots: bool, BlocksToShiverCityWithKooperShellItemThrow: bool, SewerYellowBlockWithUltraBoots: bool,
        KooperlessPleasantPathStarPiece: bool, HammerlessPleasantPathBridgeUltraBootsParakarry: bool, InvisibleBridgeClipLzs: bool, InvisibleBridgeClipLaki: bool,
        KooperlessPleasantPathThunderBolt: bool, BombettelessKbfFpPlusLZS: bool, BombettelessKbfFpPlusLaki: bool, LakiJailbreak: bool, BombettelessRightFortressJailKey: bool,
        WaterStaircaseSkip: bool, MtRuggedQuakeHammerAndLetterWithLaki: bool, ParakarrylessMtRuggedSeed: bool, BuzzarGapSkipClippy: bool, ParakarrylessMtRuggedStarPiece: bool,
        MtRuggedCoinsWithKooper: bool, MtRuggedStationJumplessClimbBombette: bool, MtRuggedStationJumplessClimbLaki: bool, MtRuggedSlideJumplessClimbLaki: bool,
        DesertBrickBlockItemWithParakarry: bool, EarlyRuinsLakiJump: bool, EarlyRuinsUltraBoots: bool, ArtifactJumpLaki: bool, ArtifactJumpUltraBoots: bool,
        RuinsKeyLakiJump: bool, ParakarrylessSecondSandRoomUltraBoots: bool, ParakarrylessSecondSandRoomNormalBoots: bool, ParakarrylessSuperHammerRoomUltraBoots: bool,
        ParakarrylessSuperHammerRoomNormalBoots: bool, RuinsLocksSkipClippy: bool, RecordSkipNoBombettePush: bool, RecordSkipBombettePush: bool, BoosPortraitWithKooper: bool,
        BoosPortraitWithLaki: bool, JumplessMansionEntry: bool, GustyGulchGateSkipLZS: bool, GustyGulchGateSkipLaki: bool, KooperlessGustyGulchDizzyDialJump: bool, KooperlessGustyGulchDizzyDialLaki: bool,
        KooperlessGustyGulchDizzyDialParakarry: bool, GustyGulchGapSkip: bool, BowlessTubbasCastle: bool, TubbasTableLakiJumpClock: bool, TubbasTableLakiJumpStudy: bool, TubbasTableUltraBoots: bool, TubbasCastleSuperBootsSkip: bool,
        ParakarrylessMegaRush: bool, ParakarrylessBlueBuildingStarPiece: bool, GourmetGuySkipJump: bool, GourmetGuySkipLaki: bool, GourmetGuySkipParakarry: bool, BowlessGreenStation: bool,
        KooperlessRedStationShootingStar: bool, GearlessRedStationShootingStar: bool, ParakarrylessBlueBlockCityGap: bool, BlueSwitchSkipLaki: bool, BlueSwitchSkipUltraBoots: bool, RedBarricadeSkip: bool, HammerlessBlueStationLaki: bool,
        HammerlessPinkStationLaki: bool, RaphSkipEnglish: bool, Ch5SushieGlitch: bool, SushielessJungleStarpieceAndLetter: bool, KooperlessLavalavaPowBlockParakarry: bool, KooperlessLavalavaPowBlockSuperBoots: bool,
        JumplessLavalavaPowBlock: bool,  UltraHammerSkip: bool, UltraHammerSkipLaki: bool, UltraHammerSkipSushie: bool,
        Flarakarry: bool, ParakarrylessFlarakarryBombette: bool, ParakarrylessFlarakarryLaki: bool, VolcanoSushieGlitch: bool, EarlyLakiLZS: bool, EarlyLakiBombettePush: bool, BombettelessMegaSmash: bool,
        SunTowerSkip: bool, YellowBerryGateSkipLZS: bool, YellowBerryGateSkipLaki: bool, YellowBerryGateSkipBombettePush: bool, RedBerryGateSkipBombettePush: bool,
        RedBerryGateSkipLaki: bool, BlueBerryGateSkipBombettePush: bool, BlueBerryGateSkipLaki: bool, BubbleBerryTreeLakiJump: bool, MurderSolvedEarlyLaki: bool,
        MurderSolvedEarlyBombettePush: bool, Ch7SushieGlitch: bool, StarStoneWithCh7SushieGlitch: bool, ShiverMountainHiddenBlockWithoutUltraBootsLaki: bool, ShiverMountainHiddenBlockWithoutUltraBootsNoLaki: bool,
        SnowmenSkipLaki: bool, ShiverMountainSwitchSkip: bool, SushielessWarehouseKeyBombette: bool, SushielessWarehouseKeyKooper: bool, MirrorClip: bool, BowlessBowsersCastleBasement: bool, BombettelessBowsersCastleBasement: bool, FastFloodRoomKooper: bool,
        FastFloodRoomBombetteUltraBoots: bool, BreakStoneBlocksWithUltraBoots: bool, BreakYellowBlocksWithSuperBoots: bool, KnowsHiddenBlocks: bool, KnowsPuzzleSolutions: bool, ReachHighBlocksWithSuperBoots: bool
        ):

        self.SeedID = SeedID
        self.SeedHashItems = get_items_from_seed_id(SeedID)
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
        self.BombetteSetting = BombetteSetting
        self.BombetteSprite = BombetteSprite
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

        self.ItemQuality = ItemQuality
        self.RandomConsumableMode = RandomConsumableMode
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
        self.GearShuffleMode = GearShuffleMode
        self.HiddenPanelVisibility = HiddenPanelVisibility
        self.CookWithoutFryingPan = CookWithoutFryingPan
        self.RipCheatoItemsInLogic = RipCheatoItemsInLogic
        self.MerlowRewardPricing = MerlowRewardPricing
        self.PrologueOpen = PrologueOpen

        if StartWithRandomPartners:
            self.RandomPartnersMax = RandomPartnersMax
            self.RandomPartnersMin = RandomPartnersMin
        else:
            self.StartWithPartners = StartWithPartners

        if WriteSpoilerLog and RevealLogInHours != 0:
            self.RevealLogAtTime = datetime.now(timezone.utc) + timedelta(hours = RevealLogInHours)

        # Glitches: Goomba Region
        self.PrologueGelEarly = PrologueGelEarly
        self.ReverseGoombaKingBridge = ReverseGoombaKingBridge
        self.GoombaVillageEntryFenceClip = GoombaVillageEntryFenceClip
        self.GoombaVillageNpcLureExit = GoombaVillageNpcLureExit
        self.HammerlessJrPlaygroundLaki = HammerlessJrPlaygroundLaki
        self.GoombaVillageLakiExit = GoombaVillageLakiExit
        self.PrologueSushieGlitchKsj = PrologueSushieGlitchKsj
        self.PrologueSushieGlitchUltraBootsLaki = PrologueSushieGlitchUltraBootsLaki

        # Glitches: Toad Town
        self.OddKeyEarly = OddKeyEarly
        self.BlueHouseSkip = BlueHouseSkip
        self.BlueHouseSkipLaki = BlueHouseSkipLaki
        self.BlueHouseSkipToadLure = BlueHouseSkipToadLure
        self.BowlessToyBoxHammer = BowlessToyBoxHammer
        self.BowlessToyBoxHammerlessLure = BowlessToyBoxHammerlessLure
        self.EarlyStoreroomParakarry = EarlyStoreroomParakarry
        self.EarlyStoreroomHammer = EarlyStoreroomHammer
        self.EarlyStoreroomHammerlessLure = EarlyStoreroomHammerlessLure
        self.WhaleEarly= WhaleEarly
        self.SushielessToadTownStarPiece = SushielessToadTownStarPiece
        self.ToadTownSushieGlitch = ToadTownSushieGlitch

        # Glitches: Toad Town Tunnels
        self.ClippyBootsStoneBlockSkip = ClippyBootsStoneBlockSkip
        self.ClippyBootsMetalBlockSkip = ClippyBootsMetalBlockSkip
        self.IslandPipeBlooperSkip = IslandPipeBlooperSkip
        self.ParakarrylessSewerStarPiece = ParakarrylessSewerStarPiece
        self.SewerBlocksWithoutUltraBoots = SewerBlocksWithoutUltraBoots
        self.FirstBlockToShiverCityWithoutSuperBoots = FirstBlockToShiverCityWithoutSuperBoots
        self.BlocksToShiverCityWithKooperShellItemThrow = BlocksToShiverCityWithKooperShellItemThrow
        self.SewerYellowBlockWithUltraBoots = SewerYellowBlockWithUltraBoots

        # Glitches: Plesant Path
        self.KooperlessPleasantPathStarPiece = KooperlessPleasantPathStarPiece
        self.HammerlessPleasantPathBridgeUltraBootsParakarry = HammerlessPleasantPathBridgeUltraBootsParakarry
        self.InvisibleBridgeClipLzs= InvisibleBridgeClipLzs
        self.InvisibleBridgeClipLaki = InvisibleBridgeClipLaki
        self.KooperlessPleasantPathThunderBolt = KooperlessPleasantPathThunderBolt

        # Glitches: Koopa Bros Fortress
        self.BombettelessKbfFpPlusLZS = BombettelessKbfFpPlusLZS
        self.BombettelessKbfFpPlusLaki = BombettelessKbfFpPlusLaki
        self.LakiJailbreak = LakiJailbreak
        self.BombettelessRightFortressJailKey = BombettelessRightFortressJailKey
        self.WaterStaircaseSkip = WaterStaircaseSkip

        # Glitches: Mt. Rugged
        self.MtRuggedQuakeHammerAndLetterWithLaki = MtRuggedQuakeHammerAndLetterWithLaki
        self.ParakarrylessMtRuggedSeed = ParakarrylessMtRuggedSeed
        self.BuzzarGapSkipClippy = BuzzarGapSkipClippy
        self.ParakarrylessMtRuggedStarPiece = ParakarrylessMtRuggedStarPiece
        self.MtRuggedCoinsWithKooper = MtRuggedCoinsWithKooper
        self.MtRuggedStationJumplessClimbBombette = MtRuggedStationJumplessClimbBombette
        self.MtRuggedStationJumplessClimbLaki = MtRuggedStationJumplessClimbLaki
        self.MtRuggedSlideJumplessClimbLaki = MtRuggedSlideJumplessClimbLaki

        # Glitches: Dry Dry Desert
        self.DesertBrickBlockItemWithParakarry = DesertBrickBlockItemWithParakarry
        self.EarlyRuinsLakiJump = EarlyRuinsLakiJump
        self.EarlyRuinsUltraBoots = EarlyRuinsUltraBoots

        # Glitches: Dry Dry Ruins
        self.ArtifactJumpLaki = ArtifactJumpLaki
        self.ArtifactJumpUltraBoots = ArtifactJumpUltraBoots
        self.RuinsKeyLakiJump = RuinsKeyLakiJump
        self.ParakarrylessSecondSandRoomUltraBoots = ParakarrylessSecondSandRoomUltraBoots
        self.ParakarrylessSecondSandRoomNormalBoots = ParakarrylessSecondSandRoomNormalBoots
        self.ParakarrylessSuperHammerRoomUltraBoots = ParakarrylessSuperHammerRoomUltraBoots
        self.ParakarrylessSuperHammerRoomNormalBoots = ParakarrylessSuperHammerRoomNormalBoots
        self.RuinsLocksSkipClippy = RuinsLocksSkipClippy

        # Glitches: Boo's Mansion
        self.RecordSkipNoBombettePush = RecordSkipNoBombettePush
        self.RecordSkipBombettePush = RecordSkipBombettePush
        self.BoosPortraitWithKooper = BoosPortraitWithKooper
        self.BoosPortraitWithLaki = BoosPortraitWithLaki
        self.JumplessMansionEntry = JumplessMansionEntry

        # Glitches: Gusty Gulch
        self.GustyGulchGateSkipLZS = GustyGulchGateSkipLZS
        self.GustyGulchGateSkipLaki = GustyGulchGateSkipLaki
        self.KooperlessGustyGulchDizzyDialJump = KooperlessGustyGulchDizzyDialJump
        self.KooperlessGustyGulchDizzyDialLaki = KooperlessGustyGulchDizzyDialLaki
        self.KooperlessGustyGulchDizzyDialParakarry= KooperlessGustyGulchDizzyDialParakarry
        self.GustyGulchGapSkip = GustyGulchGapSkip

        # Glitches: Tubba's Castle
        self.BowlessTubbasCastle = BowlessTubbasCastle
        self.TubbasTableLakiJumpClock = TubbasTableLakiJumpClock
        self.TubbasTableLakiJumpStudy = TubbasTableLakiJumpStudy
        self.TubbasTableUltraBoots = TubbasTableUltraBoots
        self.TubbasCastleSuperBootsSkip= TubbasCastleSuperBootsSkip
        self.ParakarrylessMegaRush = ParakarrylessMegaRush

        # Glitches: Toy Box
        self.ParakarrylessBlueBuildingStarPiece = ParakarrylessBlueBuildingStarPiece
        self.GourmetGuySkipJump = GourmetGuySkipJump
        self.GourmetGuySkipLaki = GourmetGuySkipLaki
        self.GourmetGuySkipParakarry = GourmetGuySkipParakarry
        self.BowlessGreenStation = BowlessGreenStation
        self.KooperlessRedStationShootingStar = KooperlessRedStationShootingStar
        self.GearlessRedStationShootingStar = GearlessRedStationShootingStar
        self.ParakarrylessBlueBlockCityGap = ParakarrylessBlueBlockCityGap
        self.BlueSwitchSkipLaki = BlueSwitchSkipLaki
        self.BlueSwitchSkipUltraBoots = BlueSwitchSkipUltraBoots
        self.RedBarricadeSkip = RedBarricadeSkip
        self.HammerlessBlueStationLaki = HammerlessBlueStationLaki
        self.HammerlessPinkStationLaki = HammerlessPinkStationLaki

        # Glitches: Jade Jungle
        self.RaphSkipEnglish = RaphSkipEnglish
        self.Ch5SushieGlitch = Ch5SushieGlitch
        self.SushielessJungleStarpieceAndLetter = SushielessJungleStarpieceAndLetter

        # Glitches: Mt. Lavalava
        self.KooperlessLavalavaPowBlockParakarry = KooperlessLavalavaPowBlockParakarry
        self.KooperlessLavalavaPowBlockSuperBoots = KooperlessLavalavaPowBlockSuperBoots
        self.JumplessLavalavaPowBlock = JumplessLavalavaPowBlock
        self.UltraHammerSkip = UltraHammerSkip
        self.UltraHammerSkipLaki = UltraHammerSkipLaki
        self.UltraHammerSkipSushie = UltraHammerSkipSushie
        self.Flarakarry = Flarakarry
        self.ParakarrylessFlarakarryBombette = ParakarrylessFlarakarryBombette
        self.ParakarrylessFlarakarryLaki = ParakarrylessFlarakarryLaki
        self.VolcanoSushieGlitch = VolcanoSushieGlitch

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
        self.StarStoneWithCh7SushieGlitch = StarStoneWithCh7SushieGlitch
        self.ShiverMountainHiddenBlockWithoutUltraBootsLaki = ShiverMountainHiddenBlockWithoutUltraBootsLaki
        self.ShiverMountainHiddenBlockWithoutUltraBootsNoLaki = ShiverMountainHiddenBlockWithoutUltraBootsNoLaki
        self.SnowmenSkipLaki  = SnowmenSkipLaki 
        self.ShiverMountainSwitchSkip = ShiverMountainSwitchSkip
        self.SushielessWarehouseKeyBombette = SushielessWarehouseKeyBombette
        self.SushielessWarehouseKeyKooper = SushielessWarehouseKeyKooper

        # Glitches: Crystal Palace
        self.MirrorClip = MirrorClip

        # Glitches: Bowser's Castle
        self.BowlessBowsersCastleBasement = BowlessBowsersCastleBasement
        self.BombettelessBowsersCastleBasement = BombettelessBowsersCastleBasement
        self.FastFloodRoomKooper = FastFloodRoomKooper
        self.FastFloodRoomBombetteUltraBoots = FastFloodRoomBombetteUltraBoots

        # Glitches: Global
        self.BreakStoneBlocksWithUltraBoots = BreakStoneBlocksWithUltraBoots
        self.BreakYellowBlocksWithSuperBoots = BreakYellowBlocksWithSuperBoots
        self.KnowsHiddenBlocks = KnowsHiddenBlocks
        self.KnowsPuzzleSolutions = KnowsPuzzleSolutions
        self.ReachHighBlocksWithSuperBoots = ReachHighBlocksWithSuperBoots

        # Other/Hidden Options
        self.SettingsName = "Default Dev Preset"
        self.SettingsVersion = "1.0.0"
        self.PrettySpoilerlog = True
        self.PlacementAlgorithm = "AssumedFill"
        self.PeachCastleReturnPipe = True # Default
        self.ChallengeMode = False # Default

    
    
