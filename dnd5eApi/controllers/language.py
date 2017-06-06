from flask_restful import Resource
from flask import jsonify

from dnd5eApi.models.language import Language as LanguageModel
from dnd5eApi.schema.language import language_schema
from dnd5eApi.schema.language import languages_schema


class Language(Resource):
    def get(self, id=None):
        if id is None:
            results = LanguageModel.query.all()
            languages = languages_schema.dump(results)
            return jsonify(languages)

        try:
            result = LanguageModel.query.get(id)
        except IntegrityError:
            return jsonify({"message": "Language could not be found."}), 400

        language = language_schema.dump(result)

        return jsonify(language.data)
