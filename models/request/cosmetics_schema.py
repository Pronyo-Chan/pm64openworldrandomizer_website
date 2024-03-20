from marshmallow import EXCLUDE, Schema, fields

class CosmeticsShema(Schema):
    class Meta:
        unknown = EXCLUDE

    SeedID = fields.Int(required=True)
