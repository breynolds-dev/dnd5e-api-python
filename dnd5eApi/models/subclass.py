from dnd5eApi import db


class Subclass(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    class_name_id = db.Column(db.Integer, db.ForeignKey('class_name.id'))
    class_name = db.relationship('ClassName')

    def __init__(self, name, description, class_name_id):
        self.name = name
        self.description = description
        self.class_name_id = class_name_id

    def __repr__(self):
        return "<Subclass: {}>".format(self.name)
