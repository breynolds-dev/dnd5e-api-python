from dnd5eApi import ma
from dnd5eApi.models.language import Language

class LanguageSchema( ma.ModelSchema ):
    class Meta:
        model = Language