# coding=utf-8
# Dungeon -> Tools

import random

import objects
import stats

# Set by config() in main.py
monsterSet = []

def generate_encounters(turns):
    """ Return a list of (Monster, Item) pairs of length TURNS."""
    encounters = []
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

        encounters.append((monster, item))
    return encounters


def generate_character():
    char = objects.Character()
    char.stats = stats.build_table(hp=100, pw=20, df=5, sp=10)
    return char


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
    if monsterSet:
        preset = random.choice(monsterSet)
        hp = preset['stat']['HP']
        pw = preset['stat']['PW']
        df = preset['stat']['DF']
        sp = preset['stat']['SP']
        monster.stats = stats.build_table(hp=hp, pw=pw, df=df, sp=sp)
        monster.name = preset['name']
        monster.desc = preset['desc']
    else:
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
