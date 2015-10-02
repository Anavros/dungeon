# Dungeon -> Tools -> Objects

import stats

class Monster(object):
    def __init__(self):
        self.name = "SCARY MONSTER"
        self.stats = stats.build_table()
    def __str__(self):
        return self.name

class Item(object):
    def __init__(self):
        self.name = "SWEET LOOT"
        self.desc = ""
        self.stackSize = 1
        self.consumable = False
        self.stats = stats.build_table()
    def __str__(self):
        return self.name
