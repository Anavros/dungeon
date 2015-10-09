# coding=utf-8
# Dungeon -> Main

import dungeon.stats as stats
import dungeon.stats.generate as generate
import dungeon.interface as interface

#XXX
import random

MAX_KEYS = 2
KEY_CHANCE = 0.5

# Untested
def begin():
    # Print an entry message
    interface.say("\nYou wander inside an old, decrepit dungeon...")
    interface.wait_for_input()

    # Generate a new character
    #character = generate.monster()
    #accessory = generate.accessory()
    character = stats.stack(generate.monster(), generate.accessory())
    keys = 0

    ###
    while True:
        (character, keys) = enter_room(character, keys)

        if character['HP'] < 0 or keys >= MAX_KEYS:
            break
    ###

    ###
    if character['HP'] > 0:
        interface.say("You have conquered the dungeon!")
    else:
        interface.say("You gave your life to destroy the dungeon.")
        interface.say("Thank you for your sacrifice.")
    ###

# Untested
def enter_room(character, keys):
    # Don't mutate the inputs!
    char = character.copy()

    # Encounter the final boss if all keys have been gathered
    if keys >= MAX_KEYS:
        mons = generate.final_boss()
    else:
        mons = generate.monster()

    # Loop the monster fight? XXX
    (char, mons) = fight(char, mons)

    if stats.crunch.chance(KEY_CHANCE):
        keys = keys + 1

    return (char, keys)


# Untested
def challenge(character, monster):
    char = character.copy()
    mons = monster.copy()
