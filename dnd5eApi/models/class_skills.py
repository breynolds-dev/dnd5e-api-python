from dnd5eApi import db

class_skills = db.Table(
    'class_skills',
    db.Column('class_id', db.Integer, db.ForeignKey('class.id')),
    db.Column('skills_id', db.Integer, db.ForeignKey('skills.id'))
)
