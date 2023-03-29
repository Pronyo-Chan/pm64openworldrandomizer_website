from marshmallow import EXCLUDE, Schema, fields

class CosmeticsShema(Schema):
    class Meta:
        unknown = EXCLUDE

    SeedID = fields.Int(required=True)

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
    LakilesterSetting = fields.Int(required=True)
    LakilesterSprite = fields.Int(required=True)
    BossesSetting = fields.Int(required=True)
    NPCSetting = fields.Int(required=True)
    EnemiesSetting = fields.Int(required=True)
    HammerSetting = fields.Int(required=True)
    MarioSetting = fields.Int(required=True)
    MarioSprite = fields.Int(required=True)
    Box5ColorA = fields.Int(required=True)
    Box5ColorB = fields.Int(required=True)
    CoinColor = fields.Int(required=True)
    RandomCoinColor = fields.Boolean(required=True)
    RomanNumerals = fields.Boolean(required=True)
    RandomPitch = fields.Boolean(required=True)
    ShuffleMusic = fields.Boolean(required=True)
    ShuffleMusicMode = fields.Int(required=True)
    ShuffleJingles = fields.Boolean(required=True)
