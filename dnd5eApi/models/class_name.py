from dnd5eApi import db
from dnd5eApi.models.class_primary_ability import class_primary_ability
from dnd5eApi.models.class_saving_throws import class_saving_throws


class ClassName(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    short_description = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    subheading_one = db.Column(db.String, nullable=False)
    subheading_two = db.Column(db.String, nullable=False)
    creating_a = db.Column(db.String, nullable=False)
    quick_build = db.Column(db.String, nullable=False)
    hit_die = db.Column(db.Integer, nullable=False)
    armor_proficiencies = db.Column(db.String, nullable=False)
    weapon_proficiencies = db.Column(db.String, nullable=False)
    tools = db.Column(db.String, nullable=False)
    skill_choice = db.Column(db.String, nullable=False)
    abilities = db.relationship('Ability', secondary='class_primary_ability')
    saving_throws = db.relationship('Ability', secondary='class_saving_throws')

    def __init__(self, name, short_description, description, subheading_one, subheading_two, creating_a, quick_build, hit_die, armor_proficiencies, weapon_proficiencies, tools, skill_choice):
        self.name = name
        self.short_description = short_description
        self.description = description
        self.subheading_one = subheading_one
        self.subheading_two = subheading_two
        self.creating_a = creating_a
        self.quick_build = quick_build
        self.hit_die = hit_die
        self.armor_proficiencies = armor_proficiencies
        self.weapon_proficiencies = weapon_proficiencies
        self.tools = tools
        self.skill_choice = skill_choice

    def __repr__(self):
        return "<Class: {}>".format(self.name)
