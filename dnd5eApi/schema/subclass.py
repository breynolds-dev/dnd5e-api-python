from marshmallow import Schema, fields
from dnd5eApi import ma, api
from dnd5eApi.models.subclass import Subclass


class SubclassSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    url = ma.AbsoluteURLFor('subclass', id='<id>')
    class_name = fields.Nested(
        'ClassNameSchema',
        attribute="class_name",
        only=['id', 'name', 'url'])


subclass_schema = SubclassSchema()
subclasses_schema = SubclassSchema(many=True, only=('id', 'name', 'url'))
