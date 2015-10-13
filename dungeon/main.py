# coding=utf-8
# Dungeon -> Main

import dungeon.stats as stats
import dungeon.stats.crunch as crunch
import dungeon.stats.generate as generate
import dungeon.interface as interface

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
        try:
            (character, keys) = enter_room(character, keys)
        except GameOverException as e:
            if e.gamewon:
                interface.say("You have conquered the dungeon!")
            else:
                interface.say("You gave your life to destroy the dungeon.")
                interface.say("Thank you for your sacrifice.")

            break

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

    while True:
        try:
            (char, mons) = step_fight(char, mons)
        except YouAreDeadException as e:
            break
        interface.say("YOU: {}".format(stats.string_repr(char)))
        interface.say("MON: {}".format(stats.string_repr(mons)))
        interface.wait_for_input()

    if crunch.chance(KEY_CHANCE):
        keys = keys + 1
        interface.say("New key!")

    return (char, keys)


# Untested
def step_fight(character, monster):
    char = character.copy()
    mons = monster.copy()
    if crunch.first_moves_first(char, mons):
        mons = crunch.damage(mons, char)
        char = crunch.damage(char, mons)
    else:
        mons = crunch.damage(mons, char)
        char = crunch.damage(char, mons)

    return (char, mons)
