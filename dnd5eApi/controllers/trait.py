from flask_restful import Resource
from flask import jsonify

from dnd5eApi.models.trait import Trait as TraitModel
from dnd5eApi.schema.trait import trait_schema
from dnd5eApi.schema.trait import traits_schema


class Trait(Resource):
    def get(self, id=None):
        if id is None:
            results = TraitModel.query.all()
            traits = traits_schema.dump(results)
            return jsonify(traits.data)

        try:
            result = TraitModel.query.get(id)
        except IntegrityError:
            return jsonify({"message": "Trait could not be found."}), 400

        trait = trait_schema.dump(result)

        return jsonify(trait.data)
