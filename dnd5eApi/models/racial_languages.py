from dnd5eApi import db

racial_languages = db.Table('racial_languages',
    db.Column('race_id', db.Integer, db.ForeignKey('race.id')),
    db.Column('language_id', db.Integer, db.ForeignKey('language.id'))
)