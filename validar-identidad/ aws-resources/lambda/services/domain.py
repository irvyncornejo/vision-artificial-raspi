from marshmallow import Schema, fields
from marshmallow.validate import OneOf, Length

class SchemaImage(Schema):
    name_image = fields.Str(required=True)
    extension = fields.Str(
        required=True,
        validate=OneOf(['png', 'jpeg'])
    )
    content = fields.Str(required=True, validate=Length(min=254))