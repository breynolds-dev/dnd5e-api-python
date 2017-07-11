#! venv/bin/python
import os

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DATABASE_URL"]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# import joins tables
from dnd5eApi.models.class_primary_ability import class_primary_ability
from dnd5eApi.models.class_saving_throws import class_saving_throws
# from dnd5eApi.models.class_skills import class_skills
from dnd5eApi.models.racial_languages import racial_languages
# from dnd5eApi.models.racial_skills import racial_skills
# from dnd5eApi.models.racial_traits import racial_traits

# import models
from dnd5eApi.models.ability import Ability
from dnd5eApi.models.class_name import ClassName
from dnd5eApi.models.feat import Feat
from dnd5eApi.models.language import Language
from dnd5eApi.models.level import Level
from dnd5eApi.models.race import Race
from dnd5eApi.models.skill import Skill
from dnd5eApi.models.subclass import Subclass
from dnd5eApi.models.trait import Trait
from dnd5eApi.models.racial_ability_bonus import RacialAbilityBonus

# create the database and the database table
db.create_all()
db.session.commit()

from seeds.abilities import Abilities
for ability in Abilities:
    new_ability = Ability(
        ability["name"],
        ability["description"],
        ability["measures"],
        ability["important_for"]
    )
    print(new_ability)
    db.session.add(new_ability)

from seeds.class_names import ClassNames
for class_name in ClassNames:
    new_class_name = ClassName(
        class_name["name"],
        class_name["short_description"],
        class_name["description"],
        class_name["subheading_one"],
        class_name["subheading_two"],
        class_name["creating_a"],
        class_name["quick_build"],
        class_name["hit_die"],
        class_name["armor_proficiencies"],
        class_name["weapon_proficiencies"],
        class_name["tools"],
        class_name["skill_choice"]
    )
    print(new_class_name)
    db.session.add(new_class_name)

from seeds.languages import Languages
for language in Languages:
    new_language = Language(
        language["name"],
        language["script"]
    )
    print(new_language)
    db.session.add(new_language)

from seeds.races import Races
for race in Races:
    new_race = Race(
        race["name"],
        race["subrace"],
        race["desc"],
        race["speed"],
        race["min_age"],
        race["max_age"],
        race["age_description"],
        race["alignment"],
        race["size"],
        race["size_description"],
        race["min_height"],
        race["max_height"],
        race["min_weight"],
        race["max_weight"],
        race["extra_skill_proficiencies"],
        race["weapon_proficiencies"],
        race["armor_proficiencies"]
    )
    print(new_race)
    db.session.add(new_race)

# # commit the changes
# db.session.commit()
    
# from seeds.racial_ability_bonuses import RacialAbilityBonuses
# for racial_ability_bonus in RacialAbilityBonuses:
#     if racial_ability_bonus["subrace"] is None:
#         new_racial_ability_bonus = RacialAbilityBonus(
#             Race.query.filter_by( name = racial_ability_bonus["race"]).first().id,
#             Ability.query.filter_by( name = racial_ability_bonus["ability"]).first().id,
#             racial_ability_bonus["bonus"]
#         )
    
#     if racial_ability_bonus["subrace"] is not None:
#         new_racial_ability_bonus = RacialAbilityBonus(
#             Race.query.filter_by( subrace = racial_ability_bonus["subrace"]).first().id,
#             Ability.query.filter_by( name = racial_ability_bonus["ability"]).first().id,
#             racial_ability_bonus["bonus"]
#         )
    
    
#     print(new_racial_ability_bonus)
#     db.session.add(new_racial_ability_bonus)

# commit the changes
db.session.commit()

# Joins Tables
from seeds.class_primary_abilities import CreateClassPrimaryAbilityRelationship
CreateClassPrimaryAbilityRelationship(db, ClassName, Ability)

from seeds.class_saving_throws import CreateClassSavingThrowsRelationship
CreateClassSavingThrowsRelationship(db, ClassName, Ability)

from seeds.racial_languages import CreateRacialLanguageRelationship
CreateRacialLanguageRelationship(db, Race, Language)

from seeds.racial_ability_bonuses import CreateRacialAbilityBonusRelationship
CreateRacialAbilityBonusRelationship(db, Race, Ability, RacialAbilityBonus)

# commit the changes
db.session.commit()
