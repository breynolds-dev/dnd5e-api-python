from dnd5eApi import db

racial_ability_bonus = db.Table('racial_ability_bonus',
    db.Column('race_id', db.Integer, db.ForeignKey('race.id')),
    db.Column('ability_id', db.Integer, db.ForeignKey('ability.id')),
    db.Columb('bonus', db.Integer )
)
