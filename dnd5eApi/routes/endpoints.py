from dnd5eApi import api
from dnd5eApi.resources.race import Race
from dnd5eApi.resources.language import Language


api.add_resource(Race, "/race", "/race/", "/race/<int:id>")
api.add_resource(Language, "/language", "/language/", "/language/<int:id>")
