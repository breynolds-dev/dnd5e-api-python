from marshmallow import Schema, fields
from dnd5eApi import ma
from dnd5eApi.models.race import Race as RaceModel

from dnd5eApi.schema.racial_ability_bonus import RacialAbilityBonusSchema


class RaceSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String()
    url = ma.AbsoluteURLFor('race', id='<id>')
    subrace = fields.String()
    desc = fields.String()
    speed = fields.Integer()
    min_age = fields.Integer()
    max_age = fields.Integer()
    age_description = fields.String()
    alignment = fields.String()
    size = fields.String()
    size_description = fields.String()
    min_height = fields.Integer()
    max_height = fields.Integer()
    min_weight = fields.Integer()
    max_weight = fields.Integer()
    extra_skill_proficiencies = fields.String()
    weapon_proficiencies = fields.String()
    armor_proficiencies = fields.String()
    languages = fields.Nested(
        'LanguageSchema',
        only=['id', 'url', 'name'],
        many=True)
    ability_bonuses = fields.Nested(
        'RacialAbilityBonusSchema',
        many=True)


race_schema = RaceSchema()
races_schema = RaceSchema(many=True, only=('id', 'name', 'subrace'))
