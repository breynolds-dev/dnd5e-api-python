from dnd5eApi import db

racial_skills = db.Table('racial_skills',
    db.Column('skills_id', db.Integer, db.ForeignKey('skills.id')),
    db.Column('trait_id', db.Integer, db.ForeignKey('trait.id'))
)
