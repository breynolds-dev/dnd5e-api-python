from dnd5eApi import db


class RacialAbilityBonus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    race_id = db.Column(db.Integer, db.ForeignKey('race.id'))
    ability_id = db.Column(db.Integer, db.ForeignKey('ability.id'))
    bonus = db.Column(db.Integer)
    ability = db.relationship('Ability')
    race = db.relationship('Race')
    
    def __init__(self, race_id, ability_id, bonus):
        self.race_id = race_id
        self.ability_id = ability_id
        self.bonus = bonus

    def __repr__(self):
        return "<RacialAbilityBonus {}>".format(race.name)
