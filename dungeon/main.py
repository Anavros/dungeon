# coding=utf-8
# Dungeon -> Main

import dungeon.stats as stats
import dungeon.stats.generate as generate
import dungeon.interface as interface

def begin():
    # Start a new game
    # Print an entry message
    # Generate a new character
    character = generate.monster()
    accessory = generate.accessory()
    keys = 0

def enter_room(character, accessory, keys):
    # Generate a new monster
    char = character.copy()
    accs = accessory.copy()
    if keys >= MAX_KEYS:
        monster = generate.final_boss()
    else:
        monster = generate.monster()

    (char, accs, monster) = fight(character, accessory, monster)

    return (character, accessory, keys)

# If all keys, generate final boss instead
# Loop the monster fight
# Chance to give key
# Fight another monster
