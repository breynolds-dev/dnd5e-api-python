from marshmallow import Schema, fields
from dnd5eApi import ma, api
from dnd5eApi.models.level import Level


class LevelSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    url = ma.AbsoluteURLFor('level', id='<id>')
    subclass = fields.Nested(
        'SubclassSchema',
        only=['id', 'name', 'url'])
    number = fields.Int()
    prof_bonus = fields.Int()
    rage_count = fields.Int()
    rage_damage_bonus = fields.Int()
    cantrips_known = fields.Int()
    spells_known = fields.Int()
    spell_slots_level_01 = fields.Int()
    spell_slots_level_02 = fields.Int()
    spell_slots_level_03 = fields.Int()
    spell_slots_level_04 = fields.Int()
    spell_slots_level_05 = fields.Int()
    spell_slots_level_06 = fields.Int()
    spell_slots_level_07 = fields.Int()
    spell_slots_level_08 = fields.Int()
    spell_slots_level_09 = fields.Int()
    martial_arts = fields.Int()
    ki_points = fields.Int()
    unarmored_movement = fields.Int()
    sneak_attack = fields.Int()
    sorcery_points = fields.Int()
    spell_slots = fields.Int()
    slot_level = fields.Int()
    invocations_known = fields.Int()


level_schema = LevelSchema()
levels_schema = LevelSchema(many=True, only=('id', 'name', 'url'))
