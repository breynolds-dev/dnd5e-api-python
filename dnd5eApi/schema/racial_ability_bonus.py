from marshmallow import Schema, fields
from dnd5eApi import ma, api
from dnd5eApi.models.race import Race
from dnd5eApi.models.ability import Ability
from dnd5eApi.models.racial_ability_bonus import RacialAbilityBonus


class RacialAbilityBonusSchema(Schema):
    bonus = fields.Int()
    ability = fields.Nested(
        'AbilitySchema',
        attribute="ability",
        only=['id', 'name', 'url'])


racial_ability_bonus_schema = RacialAbilityBonusSchema()
racial_ability_bonuses_schema = RacialAbilityBonusSchema(many=True)
