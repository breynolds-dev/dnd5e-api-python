from dnd5eApi import db
from dnd5eApi.models.racial_traits import racial_traits


class Trait(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    range = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    race = db.relationship('Race', secondary=racial_traits)

    def __init__(self, range, description):
        self.range = range
        self.description = description

    def __repr__(self):
        return "<Trait: {}>".format(self.name)
