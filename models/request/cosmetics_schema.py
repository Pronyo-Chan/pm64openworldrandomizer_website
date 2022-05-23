from marshmallow import EXCLUDE, Schema, ValidationError, fields, validates_schema, validate

CURRENT_MOD_VERSION = 4

class CosmeticsShema(Schema):
    class Meta:
        unknown = EXCLUDE

    SeedID = fields.Int()

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
    MarioSetting = fields.Int()
    MarioSprite = fields.Int()
    Box5ColorA = fields.Int()
    Box5ColorB = fields.Int()
    CoinColor = fields.Int()
    RandomCoinColor = fields.Boolean()
    RomanNumerals = fields.Boolean()
