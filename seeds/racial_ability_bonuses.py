def CreateRacialAbilityBonusRelationship(db, Race, Ability, RacialAbilityBonus):
    strength = Ability.query.filter_by(name="Strength").first()
    dexterity = Ability.query.filter_by(name="Dexterity").first()
    intelligence = Ability.query.filter_by(name="Intelligence").first()
    wisdom = Ability.query.filter_by(name="Wisdom").first()
    constitution = Ability.query.filter_by(name="Constitution").first()
    charisma = Ability.query.filter_by(name="Charisma").first()

    # == DRAGONBORN ================================================================
    race = Race.query.filter_by(name="Dragonborn").first()

    racial_ability_bonus = RacialAbilityBonus(race.id, strength.id, 2)
    race.ability_bonuses.append(racial_ability_bonus)

    racial_ability_bonus = RacialAbilityBonus(race.id, charisma.id, 1)
    race.ability_bonuses.append(racial_ability_bonus)
    db.session.merge(race)

    # == MOUNTAIN DWARF ============================================================
    race = Race.query.filter_by(subrace="Mountain Dwarf").first()

    racial_ability_bonus = RacialAbilityBonus(race.id, strength.id, 2)
    race.ability_bonuses.append(racial_ability_bonus)

    racial_ability_bonus = RacialAbilityBonus(race.id, constitution.id, 1)
    race.ability_bonuses.append(racial_ability_bonus)
    db.session.merge(race)

    # == HILL DWARF ================================================================
    race = Race.query.filter_by(subrace="Hill Dwarf").first()

    racial_ability_bonus = RacialAbilityBonus(race.id, constitution.id, 2)
    race.ability_bonuses.append(racial_ability_bonus)

    racial_ability_bonus = RacialAbilityBonus(race.id, wisdom.id, 1)
    race.ability_bonuses.append(racial_ability_bonus)
    db.session.merge(race)

    # == DUERGAR ===================================================================
    race = Race.query.filter_by(subrace="Duergar").first()

    racial_ability_bonus = RacialAbilityBonus(race.id, constitution.id, 2)
    race.ability_bonuses.append(racial_ability_bonus)

    racial_ability_bonus = RacialAbilityBonus(race.id, strength.id, 1)
    race.ability_bonuses.append(racial_ability_bonus)
    db.session.merge(race)

    # == HIGH ELF ==================================================================

    race = Race.query.filter_by(subrace="High Elf").first()

    racial_ability_bonus = RacialAbilityBonus(race.id, dexterity.id, 2)
    race.ability_bonuses.append(racial_ability_bonus)

    racial_ability_bonus = RacialAbilityBonus(race.id, intelligence.id, 1)
    race.ability_bonuses.append(racial_ability_bonus)
    db.session.merge(race)

    # == WOOD ELF ==================================================================

    race = Race.query.filter_by(subrace="Wood Elf").first()

    racial_ability_bonus = RacialAbilityBonus(race.id, dexterity.id, 2)
    race.ability_bonuses.append(racial_ability_bonus)

    racial_ability_bonus = RacialAbilityBonus(race.id, wisdom.id, 1)
    race.ability_bonuses.append(racial_ability_bonus)
    db.session.merge(race)

    # == DROW ======================================================================

    race = Race.query.filter_by(subrace="Dark Elf").first()

    racial_ability_bonus = RacialAbilityBonus(race.id, dexterity.id, 2)
    race.ability_bonuses.append(racial_ability_bonus)

    racial_ability_bonus = RacialAbilityBonus(race.id, charisma.id, 1)
    race.ability_bonuses.append(racial_ability_bonus)
    db.session.merge(race)

    # == AIR GENSAI ===============================================================

    race = Race.query.filter_by(subrace="Air Gensai").first()

    racial_ability_bonus = RacialAbilityBonus(race.id, constitution.id, 2)
    race.ability_bonuses.append(racial_ability_bonus)

    racial_ability_bonus = RacialAbilityBonus(race.id, dexterity.id, 1)
    race.ability_bonuses.append(racial_ability_bonus)
    db.session.merge(race)

    # == EARTH GENSAI ==============================================================

    race = Race.query.filter_by(subrace="Earth Gensai").first()

    racial_ability_bonus = RacialAbilityBonus(race.id, constitution.id, 2)
    race.ability_bonuses.append(racial_ability_bonus)

    racial_ability_bonus = RacialAbilityBonus(race.id, strength.id, 1)
    race.ability_bonuses.append(racial_ability_bonus)
    db.session.merge(race)

    # == FIRE GENSAI ===============================================================

    race = Race.query.filter_by(subrace="Fire Gensai").first()

    racial_ability_bonus = RacialAbilityBonus(race.id, constitution.id, 2)
    race.ability_bonuses.append(racial_ability_bonus)

    racial_ability_bonus = RacialAbilityBonus(race.id, intelligence.id, 1)
    race.ability_bonuses.append(racial_ability_bonus)
    db.session.merge(race)

    # == WATER GENSAI ==============================================================

    race = Race.query.filter_by(subrace="Water Gensai").first()

    racial_ability_bonus = RacialAbilityBonus(race.id, constitution.id, 2)
    race.ability_bonuses.append(racial_ability_bonus)

    racial_ability_bonus = RacialAbilityBonus(race.id, wisdom.id, 1)
    race.ability_bonuses.append(racial_ability_bonus)
    db.session.merge(race)

    # == DEEP GNOME ================================================================

    race = Race.query.filter_by(subrace="Deep Gnome").first()

    racial_ability_bonus = RacialAbilityBonus(race.id, intelligence.id, 2)
    race.ability_bonuses.append(racial_ability_bonus)

    racial_ability_bonus = RacialAbilityBonus(race.id, dexterity.id, 1)
    race.ability_bonuses.append(racial_ability_bonus)
    db.session.merge(race)

    # == ROCK GNOME ================================================================

    race = Race.query.filter_by(subrace="Rock Gnome").first()

    racial_ability_bonus = RacialAbilityBonus(race.id, intelligence.id, 2)
    race.ability_bonuses.append(racial_ability_bonus)

    racial_ability_bonus = RacialAbilityBonus(race.id, constitution.id, 1)
    race.ability_bonuses.append(racial_ability_bonus)
    db.session.merge(race)

    # == GOLIATH ===================================================================

    race = Race.query.filter_by(name="Goliath").first()

    racial_ability_bonus = RacialAbilityBonus(race.id, strength.id, 2)
    race.ability_bonuses.append(racial_ability_bonus)

    racial_ability_bonus = RacialAbilityBonus(race.id, constitution.id, 1)
    race.ability_bonuses.append(racial_ability_bonus)
    db.session.merge(race)

    # == LIGHTFOOT HALFLING ========================================================

    race = Race.query.filter_by(subrace="Lightfoot Halfling").first()

    racial_ability_bonus = RacialAbilityBonus(race.id, dexterity.id, 2)
    race.ability_bonuses.append(racial_ability_bonus)

    racial_ability_bonus = RacialAbilityBonus(race.id, charisma.id, 1)
    race.ability_bonuses.append(racial_ability_bonus)
    db.session.merge(race)

    # == STOUT HALFLING=============================================================

    race = Race.query.filter_by(subrace="Stout Halfling").first()

    racial_ability_bonus = RacialAbilityBonus(race.id, dexterity.id, 2)
    race.ability_bonuses.append(racial_ability_bonus)

    racial_ability_bonus = RacialAbilityBonus(race.id, constitution.id, 1)
    race.ability_bonuses.append(racial_ability_bonus)
    db.session.merge(race)

    # == GHOSTWISE HALFLING=========================================================

    race = Race.query.filter_by(subrace="Ghostwise Halfling").first()

    racial_ability_bonus = RacialAbilityBonus(race.id, dexterity.id, 2)
    race.ability_bonuses.append(racial_ability_bonus)

    racial_ability_bonus = RacialAbilityBonus(race.id, wisdom.id, 1)
    race.ability_bonuses.append(racial_ability_bonus)
    db.session.merge(race)

    # == HALF-ELF ==================================================================

    race = Race.query.filter_by(name="Half Elf").first()

    racial_ability_bonus = RacialAbilityBonus(race.id, strength.id, 2)
    race.ability_bonuses.append(racial_ability_bonus)

    racial_ability_bonus = RacialAbilityBonus(race.id, charisma.id, 1)
    race.ability_bonuses.append(racial_ability_bonus)
    db.session.merge(race)

    # == HALF-ORC ==================================================================

    race = Race.query.filter_by(name="Half Orc").first()

    racial_ability_bonus = RacialAbilityBonus(race.id, strength.id, 2)
    race.ability_bonuses.append(racial_ability_bonus)

    racial_ability_bonus = RacialAbilityBonus(race.id, constitution.id, 1)
    race.ability_bonuses.append(racial_ability_bonus)
    db.session.merge(race)

    # == HUMAN =====================================================================

    race = Race.query.filter_by(name="Human").first()

    racial_ability_bonus = RacialAbilityBonus(race.id, strength.id, 1)
    race.ability_bonuses.append(racial_ability_bonus)

    racial_ability_bonus = RacialAbilityBonus(race.id, dexterity.id, 1)
    race.ability_bonuses.append(racial_ability_bonus)

    racial_ability_bonus = RacialAbilityBonus(race.id, charisma.id, 1)
    race.ability_bonuses.append(racial_ability_bonus)

    racial_ability_bonus = RacialAbilityBonus(race.id, constitution.id, 1)
    race.ability_bonuses.append(racial_ability_bonus)

    racial_ability_bonus = RacialAbilityBonus(race.id, wisdom.id, 1)
    race.ability_bonuses.append(racial_ability_bonus)

    racial_ability_bonus = RacialAbilityBonus(race.id, intelligence.id, 1)
    race.ability_bonuses.append(racial_ability_bonus)
    db.session.merge(race)

    # == TIEFLING ==================================================================

    race = Race.query.filter_by(name="Tiefling").first()

    racial_ability_bonus = RacialAbilityBonus(race.id, charisma.id, 2)
    race.ability_bonuses.append(racial_ability_bonus)

    racial_ability_bonus = RacialAbilityBonus(race.id, intelligence.id, 1)
    race.ability_bonuses.append(racial_ability_bonus)
    db.session.merge(race)

    # == AARAKOCRA =================================================================

    race = Race.query.filter_by(name="Aarakocra").first()

    racial_ability_bonus = RacialAbilityBonus(race.id, dexterity.id, 2)
    race.ability_bonuses.append(racial_ability_bonus)

    racial_ability_bonus = RacialAbilityBonus(race.id, wisdom.id, 1)
    race.ability_bonuses.append(racial_ability_bonus)
    db.session.merge(race)
