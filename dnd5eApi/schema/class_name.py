from marshmallow import Schema, fields
from dnd5eApi import ma, api
from dnd5eApi.models.class_name import ClassName


class ClassNameSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    url = ma.AbsoluteURLFor('classname', id='<id>')
    short_description = fields.Str()
    subheading_one = fields.Str()
    subheading_two = fields.Str()
    creating_a = fields.Str()
    quick_build = fields.Str()
    hit_die = fields.Str()
    armor_proficiencies = fields.Str()
    weapon_proficiencies = fields.Str()
    tools = fields.Str()
    skill_choice = fields.Str()
    abilities = fields.Nested(
        'AbilitySchema',
        only=['id', 'name', 'url'],
        many=True)
    saving_throws = fields.Nested(
        'AbilitySchema',
        only=['id', 'name', 'url'],
        many=True)


class_name_schema = ClassNameSchema()
class_names_schema = ClassNameSchema(many=True, only=('id', 'name', 'url'))
