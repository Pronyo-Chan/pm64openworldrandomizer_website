from marshmallow import EXCLUDE, Schema, fields, validate

CURRENT_MOD_VERSION = 24

class SeedRequestSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    #Config
    StarRodModVersion = fields.Int(required=False, validate=validate.Equal(CURRENT_MOD_VERSION))
    RevealLogInHours = fields.Int(required=False, validate=validate.Range(0, 700))
