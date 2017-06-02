from flask_restful import Resource, abort
from flask import jsonify

from dnd5eApi.models.race import Race as RaceModel

class Race( Resource ):
  def get( self, race_id = None ):
    if race_id is None:
      results = []
      for row in RaceModel.query.all():

        results.append( {
          "id": row.id,
          "name": row.name,
          "subrace": row.subrace
        } )

      return jsonify( results )

    result = RaceModel.query.filter_by( id = race_id ).first()

    if not result:
      abort( 404 )
      
    racial_languages = []
    for language in result.languages:
      racial_languages.append( {
        "id": language.id,
        "name": language.name,
        "script": language.script
      } )

    response = jsonify( {
      "id": result.id,
      "name": result.name,
      "subrace": result.subrace,
      "desc": result.desc,
      "speed": result.speed,
      "min_age": result.min_age,
      "max_age": result.max_age,
      "age_description": result.age_description,
      "alignment": result.alignment,
      "size": result.size,
      "size_description": result.size_description,
      "min_height": result.min_height,
      "max_height": result.max_height,
      "min_weight": result.min_weight,
      "max_weight": result.max_weight,
      "extra_skill_proficiencies": result.extra_skill_proficiencies,
      "weapon_proficiencies": result.weapon_proficiencies,
      "armor_proficiencies": result.armor_proficiencies,
      "languages": racial_languages
    } )
    
    response.status_code = 200

    return response
