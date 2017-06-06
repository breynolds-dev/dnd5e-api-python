from marshmallow import Schema, fields
from dnd5eApi import ma, api
from dnd5eApi.models.feat import Feat


class FeatSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    url = ma.AbsoluteURLFor('feat', id='<id>')
    description = fields.Str()
    requirements = fields.Str()
    bonuses = fields.Str()
    feat = fields.Nested(
        'FeatSchema',
        attribute="feat",
        only=['id', 'name', 'url'])


feat_schema = FeatSchema()
feats_schema = FeatSchema(many=True, only=('id', 'name', 'url'))
