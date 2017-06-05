from flask_restful import Resource
from flask import jsonify

from dnd5eApi.models.race import Race as RaceModel
from dnd5eApi.schema.race import race_schema
from dnd5eApi.schema.race import races_schema


class Race(Resource):
    def get(self, id=None):
        if id is None:
            results = RaceModel.query.all()
            races = races_schema.dump(results)
            return jsonify(races.data)

        try:
            result = RaceModel.query.get(id)
        except IntegrityError:
            return jsonify({"message": "Race could not be found."}), 400

        race = race_schema.dump(result)

        return jsonify(race.data)
