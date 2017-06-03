from dnd5eApi import db
#from dnd5eApi.models.racial_languages import racial_languages

class Levels( db.Model ):
  __tablename__ = "levels"

  id = db.Column( db.Integer, primary_key = True )
  subclass_id = db.Column( db.Integer, nullable = False )
  number = db.Column( db.Integer )
  prof_bonus = db.Column( db.Integer )
  rage_count = db.Column( db.Integer )
  rage_damage_bonus = db.Column( db.Integer )
  cantrips_known = db.Column( db.Integer )
  spells_known = db.Column( db.Integer )
  spell_slots_level_01 = db.Column( db.Integer )
  spell_slots_level_02 = db.Column( db.Integer )
  spell_slots_level_03 = db.Column( db.Integer )
  spell_slots_level_04 = db.Column( db.Integer )
  spell_slots_level_05 = db.Column( db.Integer )
  spell_slots_level_06 = db.Column( db.Integer )
  spell_slots_level_07 = db.Column( db.Integer )
  spell_slots_level_08 = db.Column( db.Integer )
  spell_slots_level_09 = db.Column( db.Integer )
  martial_arts = db.Column( db.Integer )
  ki_points = db.Column( db.Integer )
  unarmored_movement = db.Column( db.Integer )
  sneak_attack = db.Column( db.Integer )
  sorcery_points = db.Column( db.Integer )
  spell_slots = db.Column( db.Integer )
  slot_level = db.Column( db.Integer )
  invocations_known = db.Column( db.Integer )
  #races = db.relationship( 'Race', secondary = racial_languages, backref = db.backref( 'language', lazy = 'dynamic' ) )

  def __init__( self, subclass_id, number, prof_bonus, rage_count, rage_damage_bonus, cantrips_known, spells_known, spell_slots, spell_slots_level_01, spell_slots_level_02, spell_slots_level_03, spell_slots_level_04, spell_slots_level_05, spell_slots_level_06, spell_slots_level_07, spell_slots_level_08, spell_slots_level_09, martial_arts, ki_points, unarmored_movement, sneak_attack, sorcery_points, slot_level, invocations_known ):
    self.subclass_id = subclass_id
    self.number = number
    self.prof_bonus = prof_bonus
    self.rage_count = rage_count
    self.rage_damage_bonus = rage_damage_bonus
    self.cantrips_known = cantrips_known
    self.spells_known = spells_known
    self.spell_slots_level_01 = spell_slots_level_01
    self.spell_slots_level_02 = spell_slots_level_02
    self.spell_slots_level_03 = spell_slots_level_03
    self.spell_slots_level_04 = spell_slots_level_04
    self.spell_slots_level_05 = spell_slots_level_05
    self.spell_slots_level_06 = spell_slots_level_06
    self.spell_slots_level_07 = spell_slots_level_07
    self.spell_slots_level_08 = spell_slots_level_08
    self.spell_slots_level_09 = spell_slots_level_09
    self.martial_arts = martial_arts
    self.ki_points = ki_points
    self.unarmored_movement = unarmored_movement
    self.sneak_attack = sneak_attack
    self.sorcery_points = sorcery_points
    self.spell_slots = spell_slots
    self.slot_level = slot_level
    self.invocations_known = invocations_known

  def __repr__( self ):
    return "<Levels: {}>".format( self.name )
