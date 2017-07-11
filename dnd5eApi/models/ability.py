from dnd5eApi import db
from dnd5eApi.models.class_primary_ability import class_primary_ability
from dnd5eApi.models.racial_ability_bonus import RacialAbilityBonus


class Ability(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    measures = db.Column(db.String, nullable=False)
    important_for = db.Column(db.String, nullable=False)
    classes = db.relationship('ClassName', secondary=class_primary_ability)
    races = db.relationship('RacialAbilityBonus', backref="abilities", primaryjoin= id == RacialAbilityBonus.ability_id)

    def __init__(self, name, description, measures, important_for):
        self.name = name
        self.description = description
        self.measures = measures
        self.important_for = important_for

    def __repr__(self):
        return "<Ability: {}>".format(self.name)
