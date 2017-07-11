from dnd5eApi import db

class_skills = db.Table(
    'class_skills',
    db.Column('class_name_id', db.Integer, db.ForeignKey('class_name.id')),
    db.Column('skills_id', db.Integer, db.ForeignKey('skills.id'))
)
