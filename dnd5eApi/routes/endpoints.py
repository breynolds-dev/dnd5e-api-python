from dnd5eApi import api

# Controller Imports
from dnd5eApi.controllers.ability import Ability
from dnd5eApi.controllers.class_name import ClassName
from dnd5eApi.controllers.feat import Feat
from dnd5eApi.controllers.language import Language
from dnd5eApi.controllers.race import Race
from dnd5eApi.controllers.skill import Skill
from dnd5eApi.controllers.trait import Trait

# API Endpoints
api.add_resource(Ability, "/ability", "/ability/", "/ability/<int:id>")
api.add_resource(ClassName, "/class", "/class/", "/class/<int:id>")
api.add_resource(Feat, "/feat", "/feat/", "/feat/<int:id>")
api.add_resource(Language, "/language", "/language/", "/language/<int:id>")
api.add_resource(Race, "/race", "/race/", "/race/<int:id>")
api.add_resource(Skill, "/skill", "/skill/", "/skill/<int:id>")
api.add_resource(Trait, "/trait", "/trait/", "/trait/<int:id>")
