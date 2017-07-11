from dnd5eApi import db

class_saving_throws = db.Table(
    'class_saving_throws',
    db.Column('class_name_id', db.Integer, db.ForeignKey('class_name.id')),
    db.Column('ability_id', db.Integer, db.ForeignKey('ability.id'))
)
