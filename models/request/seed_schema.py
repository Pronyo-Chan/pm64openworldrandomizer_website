from datetime import datetime
from marshmallow import Schema, ValidationError, fields, validates_schema, validate

def validate_random_partners(n):
    if n < 0:
        raise ValidationError("Quantity must be greater than 0.")
    if n > 30:
        raise ValidationError("Quantity must not be greater than 30.")

class StartWithPartnersSchema(Schema):

    Goombario: fields.Boolean()
    Kooper: fields.Boolean()
    Bombette: fields.Boolean()
    Bow: fields.Boolean()
    Watt: fields.Boolean()
    Sushie: fields.Boolean()
    Lakilester: fields.Boolean()

class SeedRequestSchema(Schema):
    StarRodModVersion = fields.Int()
    AlwaysSpeedySpin = fields.Boolean()
    AlwaysISpy = fields.Boolean()
    AlwaysPeekaboo = fields.Boolean()
    HiddenBlockMode = fields.Int(validate=validate.Range(0, 3))
    AllowPhysicsGlitches = fields.Boolean()
    InitialCoins = fields.Int(default=validate.Range(0, 999))
    CapEnemyXP = fields.Boolean()
    NoXP = fields.Boolean()
    DoubleDamage = fields.Boolean()
    QuadrupleDamage = fields.Boolean()
    OHKO = fields.Boolean()
    NoSaveBlocks = fields.Boolean()
    NoHeartBlock = fields.Boolean()
    FlowerGateOpen = fields.Boolean()
    BlueHouseOpen = fields.Boolean()
    ToyboxOpen = fields.Boolean()
    WhaleOpen = fields.Boolean()
    ShuffleChapterDifficulty = fields.Boolean()
    ProgressiveScaling = fields.Boolean()
    RandomFormations = fields.Boolean()
    ShuffleItems = fields.Boolean()
    IncludeCoins = fields.Boolean()
    IncludeShops = fields.Boolean()
    IncludePanels = fields.Boolean()
    IncludeFavors = fields.Boolean()
    IncludeLetterChain = fields.Boolean()
    KeyitemsOutsideDungeon = fields.Boolean()
    ShuffleBadgesBP = fields.Boolean()
    ShuffleBadgesFP = fields.Boolean()
    ShufflePartnerFP = fields.Boolean()
    ShuffleStarpowerSP = fields.Boolean()
    RandomQuiz = fields.Boolean()
    SkipQuiz = fields.Boolean()
    QuizmoAlwaysAppears = fields.Boolean()
    PartnersInDefaultLocations = fields.Boolean()
    PartnersAlwaysUsable = fields.Boolean()
    StartWithRandomPartners = fields.Boolean()
    RandomPartnersMin = fields.Int(validate = validate.Range(1, 8))
    RandomPartnersMax= fields.Int(validate = validate.Range(1, 8))

    StartWithPartners = fields.Nested(StartWithPartnersSchema)

    WriteSpoilerLog = fields.Boolean()
    RandomCoinPalette = fields.Boolean()
    RomanNumerals = fields.Boolean()
    TurnOffMusic = fields.Boolean()
    IncludeDojo = fields.Boolean()

    @validates_schema
    def validate_random_partners(self, data, **kwargs):
        if data["RandomPartnersMin"] > data["RandomPartnersMax"]:
            raise ValidationError("field_a must be greater than field_b")