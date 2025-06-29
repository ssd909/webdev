from marshmallow import fields, schema, Schema


class LoginSchema(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)
