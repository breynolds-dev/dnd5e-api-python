def CreateRacialLanguageRelationship( db, Race, Language ):
# == DRAGONBORN ================================================================
  race = Race.query.filter_by( name = "Dragonborn" ).first()
  language = Language.query.filter_by( name = "Common" ).first()
  racial_language = race.languages.append( language )
  language = Language.query.filter_by( name = "Draconic" ).first()
  racial_language = race.languages.append( language )
  db.session.merge(race)
  
# == MOUNTAIN DWARF ============================================================
  race = Race.query.filter_by( subrace = "Mountain Dwarf" ).first()
  language = Language.query.filter_by( name = "Common" ).first()
  racial_language = race.languages.append( language )
  language = Language.query.filter_by( name = "Dwarvish" ).first()
  racial_language = race.languages.append( language )
  db.session.merge(race)
  
# == HILL DWARF ================================================================
  race = Race.query.filter_by( subrace = "Hill Dwarf" ).first()
  language = Language.query.filter_by( name = "Common" ).first()
  racial_language = race.languages.append( language )
  language = Language.query.filter_by( name = "Dwarvish" ).first()
  racial_language = race.languages.append( language )
  db.session.merge(race)
  
# == DUERGAR ===================================================================
  race = Race.query.filter_by( subrace = "Duergar" ).first()
  language = Language.query.filter_by( name = "Common" ).first()
  racial_language = race.languages.append( language )
  language = Language.query.filter_by( name = "Dwarvish" ).first()
  racial_language = race.languages.append( language )
  language = Language.query.filter_by( name = "Undercommon" ).first()
  racial_language = race.languages.append( language )
  db.session.merge(race)

# == HIGH ELF ==================================================================

  race = Race.query.filter_by( subrace = "High Elf" ).first()
  language = Language.query.filter_by( name = "Common" ).first()
  racial_language = race.languages.append( language )
  language = Language.query.filter_by( name = "Elvish" ).first()
  racial_language = race.languages.append( language )
  db.session.merge(race)

# == WOOD ELF ==================================================================

  race = Race.query.filter_by( subrace = "Wood Elf" ).first()
  language = Language.query.filter_by( name = "Common" ).first()
  racial_language = race.languages.append( language )
  language = Language.query.filter_by( name = "Elvish" ).first()
  racial_language = race.languages.append( language )
  db.session.merge(race)

# == DROW ======================================================================

  race = Race.query.filter_by( subrace = "Dark Elf" ).first()
  language = Language.query.filter_by( name = "Common" ).first()
  racial_language = race.languages.append( language )
  language = Language.query.filter_by( name = "Elvish" ).first()
  racial_language = race.languages.append( language )
  language = Language.query.filter_by( name = "Undercommon" ).first()
  racial_language = race.languages.append( language )
  db.session.merge(race)

# == AIR GENSAI ===============================================================

  race = Race.query.filter_by( subrace = "Air Gensai" ).first()
  language = Language.query.filter_by( name = "Common" ).first()
  racial_language = race.languages.append( language )
  language = Language.query.filter_by( name = "Primordial" ).first()
  racial_language = race.languages.append( language )
  db.session.merge(race)

# == EARTH GENSAI ==============================================================

  race = Race.query.filter_by( subrace = "Earth Gensai" ).first()
  language = Language.query.filter_by( name = "Common" ).first()
  racial_language = race.languages.append( language )
  language = Language.query.filter_by( name = "Primordial" ).first()
  racial_language = race.languages.append( language )
  db.session.merge(race)

# == FIRE GENSAI ===============================================================

  race = Race.query.filter_by( subrace = "Fire Gensai" ).first()
  language = Language.query.filter_by( name = "Common" ).first()
  racial_language = race.languages.append( language )
  language = Language.query.filter_by( name = "Primordial" ).first()
  racial_language = race.languages.append( language )
  db.session.merge(race)

# == WATER GENSAI ==============================================================

  race = Race.query.filter_by( subrace = "Water Gensai" ).first()
  language = Language.query.filter_by( name = "Common" ).first()
  racial_language = race.languages.append( language )
  language = Language.query.filter_by( name = "Primordial" ).first()
  racial_language = race.languages.append( language )
  db.session.merge(race)

# == DEEP GNOME ================================================================

  race = Race.query.filter_by( subrace = "Deep Gnome" ).first()
  language = Language.query.filter_by( name = "Gnomish" ).first()
  racial_language = race.languages.append( language )
  language = Language.query.filter_by( name = "Undercommon" ).first()
  racial_language = race.languages.append( language )
  language = Language.query.filter_by( name = "Common" ).first()
  racial_language = race.languages.append( language )
  db.session.merge(race)

# == ROCK GNOME ================================================================

  race = Race.query.filter_by( subrace = "Rock Gnome" ).first()
  language = Language.query.filter_by( name = "Common" ).first()
  racial_language = race.languages.append( language )
  language = Language.query.filter_by( name = "Gnomish" ).first()
  racial_language = race.languages.append( language )
  db.session.merge(race)

# == GOLIATH ===================================================================

  race = Race.query.filter_by( name = "Goliath" ).first()
  language = Language.query.filter_by( name = "Common" ).first()
  racial_language = race.languages.append( language )
  language = Language.query.filter_by( name = "Giant" ).first()
  racial_language = race.languages.append( language )
  db.session.merge(race)

# == LIGHTFOOT HALFLING ========================================================

  race = Race.query.filter_by( subrace = "Lightfoot Halfling" ).first()
  language = Language.query.filter_by( name = "Common" ).first()
  racial_language = race.languages.append( language )
  db.session.merge(race)

# == STOUT HALFLING=============================================================

  race = Race.query.filter_by( subrace = "Stout Halfling" ).first()
  language = Language.query.filter_by( name = "Common" ).first()
  racial_language = race.languages.append( language )
  db.session.merge(race)

# == GHOSTWISE HALFLING=========================================================

  race = Race.query.filter_by( subrace = "Ghostwise Halfling" ).first()
  language = Language.query.filter_by( name = "Common" ).first()
  racial_language = race.languages.append( language )
  db.session.merge(race)

# == HALF-ELF ==================================================================

  race = Race.query.filter_by( name = "Half Elf" ).first()
  language = Language.query.filter_by( name = "Common" ).first()
  racial_language = race.languages.append( language )
  language = Language.query.filter_by( name = "Elvish" ).first()
  racial_language = race.languages.append( language )
  db.session.merge(race)

# == HALF-ORC ==================================================================

  race = Race.query.filter_by( name = "Half Orc" ).first()
  language = Language.query.filter_by( name = "Common" ).first()
  racial_language = race.languages.append( language )
  language = Language.query.filter_by( name = "Goblin" ).first()
  racial_language = race.languages.append( language )
  db.session.merge(race)

# == HUMAN =====================================================================

  race = Race.query.filter_by( name = "Human" ).first()
  language = Language.query.filter_by( name = "Common" ).first()
  racial_language = race.languages.append( language )
  db.session.merge(race)

# == TIEFLING ==================================================================

  race = Race.query.filter_by( name = "Tiefling" ).first()
  language = Language.query.filter_by( name = "Common" ).first()
  racial_language = race.languages.append( language )
  language = Language.query.filter_by( name = "Infernal" ).first()
  racial_language = race.languages.append( language )
  db.session.merge(race)

# == AARAKOCRA =================================================================

  race = Race.query.filter_by( name = "Aarakocra" ).first()
  language = Language.query.filter_by( name = "Common" ).first()
  racial_language = race.languages.append( language )
  language = Language.query.filter_by( name = "Aarakocra" ).first()
  racial_language = race.languages.append( language )
  language = Language.query.filter_by( name = "Auran" ).first()
  racial_language = race.languages.append( language )
  db.session.merge(race)