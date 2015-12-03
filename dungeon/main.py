# coding=utf-8
# Dungeon -> Main

import malt
import dungeon.core as stats
import dungeon.crunch as crunch
import dungeon.generate as generate

MAX_KEYS = 2
KEY_CHANCE = 0.5

def begin():
    malt.show("\nYou wander inside an old, decrepit dungeon...")
    malt.pause()

    # Generate a new character
    character = stats.stack(generate.monster(), generate.accessory())
    keys = 0

    ###
    while True:
        try:
            (character, keys) = enter_room(character, keys)
        except GameOverException as e:
            if e.gamewon:
                malt.show("You have conquered the dungeon!")
            else:
                malt.show("You gave your life to destroy the dungeon.")
                malt.show("Thank you for your sacrifice.")

            break

        if character['HP'] < 0 or keys >= MAX_KEYS:
            break
    ###

    ###
    if character['HP'] > 0:
        malt.show("You have conquered the dungeon!")
    else:
        malt.show("You gave your life to destroy the dungeon.")
        malt.show("Thank you for your sacrifice.")
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
        malt.show("YOU: {}".format(stats.string_repr(char)))
        malt.show("MON: {}".format(stats.string_repr(mons)))
        malt.pause()

    if crunch.chance(KEY_CHANCE):
        keys = keys + 1
        malt.show("New key!")

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
