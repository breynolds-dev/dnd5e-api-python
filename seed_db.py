#! venv/bin/python
import os

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask( __name__ )
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DATABASE_URL"]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy( app )

# import joins tables
from dnd5eApi.models.racial_languages import racial_languages

# import models
from dnd5eApi.models.language import Language
from dnd5eApi.models.race import Race

# create the database and the database table
db.create_all()
db.session.commit()

from seeds.languages import Languages
for language in Languages:
  new_language = Language( language["name"], language["script"] )
  print( new_language )
  db.session.add( new_language )
  
from seeds.races import Races
for race in Races:
  new_race = Race( race["name"], race["subrace"], race["desc"], race["speed"], race["min_age"], race["max_age"], race["age_description"], race["alignment"], race["size"], race["size_description"], race["min_height"], race["max_height"], race["min_weight"], race["max_weight"], race["extra_skill_proficiencies"], race["weapon_proficiencies"], race["armor_proficiencies"] )
  print( new_race )
  db.session.add( new_race )
  
# commit the changes
db.session.commit()
 
# Joins Tables
from seeds.racial_languages import CreateRacialLanguageRelationship

CreateRacialLanguageRelationship( db, Race, Language )

# commit the changes
db.session.commit()