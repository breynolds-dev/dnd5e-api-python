from flask_restful import Resource
from flask import jsonify

from dnd5eApi.models.skill import Skill as SkillModel
from dnd5eApi.schema.skill import skill_schema
from dnd5eApi.schema.skill import skills_schema


class Skill(Resource):
    def get(self, id=None):
        if id is None:
            results = SkillModel.query.all()
            skills = skills_schema.dump(results)
            return jsonify(skills.data)

        try:
            result = SkillModel.query.get(id)
        except IntegrityError:
            return jsonify({"message": "Skill could not be found."}), 400

        skill = skill_schema.dump(result)

        return jsonify(skill.data)
