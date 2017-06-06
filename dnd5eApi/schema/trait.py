from marshmallow import Schema, fields
from dnd5eApi import ma, api
from dnd5eApi.models.trait import Trait


class TraitSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    url = ma.AbsoluteURLFor('trait', id='<id>')
    range = fields.Str()
    description = fields.Str()
    race = fields.Nested(
        'RaceSchema',
        attribute="race",
        only=['id', 'name', 'url'])


trait_schema = TraitSchema()
traits_schema = TraitSchema(many=True, only=('id', 'name', 'url'))
