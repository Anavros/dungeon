# Dungeon -> Tools -> Objects

import copy
import stats

class Actor(object):
    def __init__(self):
        self.name = "GENERIC ACTOR"
        self.stats = stats.build_table()
    def __str__(self):
        return self.name
    def copy(self):
        return copy.deepcopy(self)


class Monster(Actor):
    def __init__(self):
        self.name = "SCARY MONSTER"


class Character(Actor):
    def __init__(self):
        self.name = "Bogart the Adventurer"
        self.inventory = []
    def is_alive(self):
        return self.stats['HP'] > 0


class Item(object):
    def __init__(self):
        self.name = "SWEET LOOT"
        self.desc = ""
        self.stackSize = 1
        self.consumable = False
        self.stats = stats.build_table()
    def __str__(self):
        return self.name
