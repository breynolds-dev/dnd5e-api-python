from dnd5eApi import db


class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    ability_id = db.Column(db.Integer, db.ForeignKey('ability.id'))
    ability = db.relationship('Ability')

    def __init__(self, name, description, ability_id):
        self.name = name
        self.description = description
        self.ability_id = ability_id

    def __repr__(self):
        return "<Skill: {}>".format(self.name)
