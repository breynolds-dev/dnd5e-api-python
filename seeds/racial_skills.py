# == DRAGONBORN ================================================================

# Data

# == MOUNTAIN DWARF ============================================================

# Data

# == HILL DWARF ================================================================

# Data

# == DUERGAR ===================================================================

# Data

# == HIGH ELF ==================================================================

RacialSkill.create(
  race_id: Race.find_by(subrace: 'High Elf').id,
  skill_id: Skill.find_by(name: 'Perception').id
)

# == WOOD ELF ==================================================================

RacialSkill.create(
  race_id: Race.find_by(subrace: 'Wood Elf').id,
  skill_id: Skill.find_by(name: 'Perception').id
)

# == DROW ======================================================================

RacialSkill.create(
  race_id: Race.find_by(subrace: 'Dark Elf').id,
  skill_id: Skill.find_by(name: 'Perception').id
)

# == GENSAI ====================================================================

# Data

# == DEEP GNOME ================================================================

# Data

# == ROCK GNOME ================================================================

# Data

# == GOLIATH ===================================================================

RacialSkill.create(
  race_id: Race.find_by(name: 'Goliath').id,
  skill_id: Skill.find_by(name: 'Athletics').id
)

# == LIGHTFOOT HALFLING ========================================================

# Data

# == STOUT HALFLING=============================================================

# Data

# == GHOSTWISE HALFLING=========================================================

# Data

# == HALF-ELF ==================================================================

# Data

# == HALF-ORC ==================================================================

# Data

# == HUMAN =====================================================================

# Data

# == TIEFLING ==================================================================

# Data
