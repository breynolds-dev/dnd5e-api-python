from dnd5eApi import db

class_primary_ability = db.Table(
    'class_primary_ability',
    db.Column('class_name.id', db.Integer, db.ForeignKey('class_name.id')),
    db.Column('ability_id', db.Integer, db.ForeignKey('ability.id'))
)
