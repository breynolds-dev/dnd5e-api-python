from flask_restful import Resource
from flask import jsonify

from dnd5eApi.models.ability import Ability as AbilityModel
from dnd5eApi.schema.ability import ability_schema
from dnd5eApi.schema.ability import abilities_schema


class Ability(Resource):
    def get(self, id=None):
        if id is None:
            results = AbilityModel.query.all()
            abilities = abilities_schema.dump(results)
            return jsonify(abilities.data)

        try:
            result = AbilityModel.query.get(id)
        except IntegrityError:
            return jsonify({"message": "Ability could not be found."}), 400

        ability = ability_schema.dump(result)

        return jsonify(ability.data)
