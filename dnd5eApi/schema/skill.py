from marshmallow import Schema, fields
from dnd5eApi import ma, api
from dnd5eApi.models.skill import Skill


class SkillSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    url = ma.AbsoluteURLFor('skill', id='<id>')
    description = fields.Str()
    skill = fields.Nested(
        'SkillSchema',
        attribute="skill",
        only=['id', 'name', 'url'])


skill_schema = SkillSchema()
skills_schema = SkillSchema(many=True, only=('id', 'name', 'url'))
