from marshmallow import Schema, fields
from dnd5eApi import ma, api
from dnd5eApi.models.language import Language


class LanguageSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    url = ma.AbsoluteURLFor('language', id='<id>')
    script = fields.Str()
    native_speakers = fields.Nested(
        'RaceSchema',
        attribute="races",
        only=['id', 'name', 'subrace', 'url'],
        many=True)


language_schema = LanguageSchema()
languages_schema = LanguageSchema(many=True, only=('id', 'name', 'url'))
