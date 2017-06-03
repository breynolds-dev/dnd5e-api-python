from dnd5eApi import db
from dnd5eApi.models.racial_traits import racial_traits

class Trait( db.Model ):
  __tablename__ = "traits"

  id = db.Column( db.Integer, primary_key = True )
  range_ = db.Column( db.String, nullable = False )
  description = db.Column( db.String, nullable = False )
  race_name = db.relationship( 'Race', secondary = racial, backref = db.backref( 'traits', lazy = 'dynamic' ) )

  def __init__( self, range_, description, ability ):
    self.range_ = range_
    self.description = description

  def __repr__( self ):
    return "<Traits: {}>".format( self.name )
