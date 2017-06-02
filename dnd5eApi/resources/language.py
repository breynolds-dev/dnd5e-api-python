from flask_restful import Resource, abort
from flask import jsonify

from dnd5eApi.models.language import Language as LanguageModel

class Language( Resource ):
  def get( self, language_id = None ):
    if language_id is None:
      results = []
      for row in LanguageModel.query.all():

        results.append( {
          "id": row.id,
          "name": row.name
        } )

      return jsonify( results )

    result = LanguageModel.query.filter_by( id = language_id ).first()

    if not result:
      abort( 404 )
      
    racial_languages = []
    for race in result.races:
      racial_languages.append( {
        "id": race.id,
        "name": race.name,
        "subrace": race.subrace
      } )

    response = jsonify( {
      "id": result.id,
      "name": result.name,
      "script": result.script,
      "native_speakers": racial_languages
    } )
    
    response.status_code = 200

    return response
