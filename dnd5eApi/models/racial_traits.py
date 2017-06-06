from dnd5eApi import db

racial_traits = db.Table('racial_traits',
    db.Column('race_id', db.Integer, db.ForeignKey('race.id')),
    db.Column('trait_id', db.Integer, db.ForeignKey('trait.id'))
)
