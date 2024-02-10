from marshmallow import EXCLUDE, Schema, fields, validate

CURRENT_MOD_VERSION = 22

class SeedRequestSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    #Config
    StarRodModVersion = fields.Int(required=True, validate=validate.Equal(CURRENT_MOD_VERSION))
    SettingsString = fields.String(required=True)
    RevealLogInHours = fields.Int(required=True, validate=validate.Range(0, 700))
