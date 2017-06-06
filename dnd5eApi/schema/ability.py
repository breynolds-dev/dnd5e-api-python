from marshmallow import Schema, fields
from dnd5eApi import ma, api
from dnd5eApi.models.ability import Ability


class AbilitySchema(Schema):
    id = fields.Int()
    name = fields.Str()
    url = ma.AbsoluteURLFor('ability', id='<id>')
    description = fields.Str()
    measures = fields.Str()
    important_for = fields.Str()
    classes = fields.Nested(
        'ClassNameSchema',
        attribute="class_name",
        only=['id', 'name', 'url'],
        many=True)


ability_schema = AbilitySchema()
abilities_schema = AbilitySchema(many=True, only=('id', 'name', 'url'))
