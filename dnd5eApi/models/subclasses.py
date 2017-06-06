from dnd5eApi import db
#from dnd5eApi.models.racial_languages import class_skills

class Skill( db.Model ):
  __tablename__ = "skills"

  id = db.Column( db.Integer, primary_key = True )
  name = db.Column( db.String, nullable = False )
  description = db.Column( db.String, nullable = False )
  #class_name_id = db.relationship( 'Class', secondary = class_skills, backref = db.backref( 'skills', lazy = 'dynamic' ) )

  def __init__( self, name, description, ability ):
    self.name = name
    self.description = description

  def __repr__( self ):
    return "<Skills: {}>".format( self.name )
