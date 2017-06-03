from dnd5eApi import db

class_primary_ability = db.Table('class_primary_ability',
    db.Column('className_id', db.Integer, db.ForeignKey('className.id')),
    db.Column('ability_id', db.Integer, db.ForeignKey('ability.id'))
)
