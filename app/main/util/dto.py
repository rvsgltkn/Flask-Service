from marshmallow import Schema, fields


class TaskContentSchema(Schema):
    text=fields.String(required=True)
    created_on=fields.Date( required=False)
    updated_on=fields.Date( required=False)





