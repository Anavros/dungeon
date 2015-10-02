# Dungeon -> Tools

import queue
import random

import objects
import stats

def generate_encounters(turns):
    """ Return a queue of (Monster, Item) pairs of length TURNS."""
    encounters = queue.Queue()
    itemWeights = [("Armor", 2), ("Weapon", 4), ("Potion", 4)]
    itemPop = [item for (item, weight) in itemWeights for i in range(weight)]

    for i in range(turns):
        item = None
        itemType = random.choice(itemPop)
        if itemType == "Armor":
            item = generate_armor()
        elif itemType == "Weapon":
            item = generate_weapon()
        elif itemType == "Potion":
            item = generate_potion()
        else:
            assert False, "You done messed up"

        monster = generate_monster()

        encounters.put((monster, item))
    return encounters


def generate_final_boss():
    monster = objects.Monster()
    monster.stats = stats.build_table(hp=100, pw=5, df=5, sp=8)
    monster.name = "Spookazoran the Scary Dungeon Boss"
    return monster

def generate_treasure():
    treasure = objects.Item()
    return treasure


def generate_monster():
    monster = objects.Monster()
    monster.stats = stats.build_table(hp=10, pw=2, df=2, sp=3)
    monster.name = "Monster Peon"
    return monster


def generate_armor():
    armor = objects.Item()
    armor.stats = stats.build_table(df=10, sp=-10)
    return armor


def generate_weapon():
    weapon = objects.Item()
    weapon.stats = stats.build_table(pw=10)
    return weapon


def generate_potion():
    potion = objects.Item()
    potion.consumable = True
    potion.stackSize = 24
    potion.stats = stats.build_table(hp=5)
    return potion
