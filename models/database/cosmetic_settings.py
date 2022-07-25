
class CosmeticSettings:

    def __init__(self, SeedID: str, RomanNumerals: bool = False, RandomText: bool = False, Box5ColorA: int = 0xEBE677FF, Box5ColorB: int = 0x8E5A25FF, RandomCoinColor: bool = False, \
        CoinColor: int = 0, MarioSetting: int = 0, MarioSprite: int = 0, GoombarioSetting: int = 0, GoombarioSprite: int = 0, KooperSetting: int = 0, \
        KooperSprite: int = 0, BowSetting: int = 0, BowSprite: int = 0, BossesSetting: int = 0, NPCSetting: int = 0, EnemiesSetting: int = 0, WattSetting: int = 0, WattSprite: int = 0, \
        SushieSetting: int = 0, SushieSprite: int = 0, ParakarrySetting: int = 0, ParakarrySprite: int = 0, RandomPitch: bool = False):

        self.SeedID = SeedID
        self.Box5ColorA = Box5ColorA
        self.Box5ColorB = Box5ColorB
        self.RandomCoinColor = RandomCoinColor
        self.CoinColor = CoinColor        
        self.RandomText = RandomText        
        self.RomanNumerals = RomanNumerals

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

        self.RandomPitch = RandomPitch
    
    