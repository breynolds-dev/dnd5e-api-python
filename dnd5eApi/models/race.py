from dnd5eApi import db
from dnd5eApi.models.racial_languages import racial_languages
from dnd5eApi.models.racial_ability_bonus import RacialAbilityBonus


class Race(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    subrace = db.Column(db.String)
    desc = db.Column(db.String)
    speed = db.Column(db.Integer)
    min_age = db.Column(db.Integer)
    max_age = db.Column(db.Integer)
    age_description = db.Column(db.String)
    alignment = db.Column(db.String)
    size = db.Column(db.String)
    size_description = db.Column(db.String)
    min_height = db.Column(db.Integer)
    max_height = db.Column(db.Integer)
    min_weight = db.Column(db.Integer)
    max_weight = db.Column(db.Integer)
    extra_skill_proficiencies = db.Column(db.Integer)
    weapon_proficiencies = db.Column(db.String)
    armor_proficiencies = db.Column(db.String)
    languages = db.relationship('Language', secondary=racial_languages)
    ability_bonuses = db.relationship('RacialAbilityBonus', backref="races", primaryjoin= id == RacialAbilityBonus.race_id)

    def __init__(self, name, subrace, desc, speed, min_age, max_age, age_description, alignment, size, size_description, min_height, max_height, min_weight, max_weight, extra_skill_proficiencies, weapon_proficiencies, armor_proficiencies):
        self.name = name
        self.subrace = subrace
        self.desc = desc
        self.speed = speed
        self.min_age = min_age
        self.max_age = max_age
        self.age_description = age_description
        self.alignment = alignment
        self.size = size
        self.size_description = size_description
        self.min_height = min_height
        self.max_height = max_height
        self.min_weight = min_weight
        self.max_weight = max_weight
        self.extra_skill_proficiencies = extra_skill_proficiencies
        self.weapon_proficiencies = weapon_proficiencies
        self.armor_proficiencies = armor_proficiencies

    def __repr__(self):
        return "<Race: {} Subrace: {}>".format(self.name, self.subrace)
