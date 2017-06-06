from dnd5eApi import db


class Feat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    requirements = db.Column(db.String, nullable=False)
    bonuses = db.Column(db.String, nullable=False)

    def __init__(self, name, description, requirements, bonuses):
        self.name = name
        self.description = description
        self.requirements = requirements
        self.bonuses = bonuses

    def __repr__(self):
        return "<Feat: {}>".format(self.name)
