from flask_restful import Resource
from flask import jsonify

from dnd5eApi.models.feat import Feat as FeatModel
from dnd5eApi.schema.feat import feat_schema
from dnd5eApi.schema.feat import feats_schema


class Feat(Resource):
    def get(self, id=None):
        if id is None:
            results = FeatModel.query.all()
            feats = feats_schema.dump(results)
            return jsonify(feats.data)

        try:
            result = FeatModel.query.get(id)
        except IntegrityError:
            return jsonify({"message": "Feat could not be found."}), 400

        feat = feat_schema.dump(result)

        return jsonify(feat.data)
