from flask_restful import Resource
from flask import jsonify

from dnd5eApi.models.class_name import ClassName as ClassNameModel
from dnd5eApi.schema.class_name import class_name_schema
from dnd5eApi.schema.class_name import class_names_schema


class ClassName(Resource):
    def get(self, id=None):
        if id is None:
            results = ClassNameModel.query.all()
            class_names = class_names_schema.dump(results)
            return jsonify(class_names.data)

        try:
            result = ClassNameModel.query.get(id)
        except IntegrityError:
            return jsonify({"message": "ClassName could not be found."}), 400

        class_name = class_name_schema.dump(result)

        return jsonify(class_name.data)
