from dnd5eApi import ma
from dnd5eApi.models.race import Race

class RaceSchema( ma.ModelSchema ):
    class Meta:
        model = Race