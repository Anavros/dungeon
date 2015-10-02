# Dungeon -> Tools

import queue

__all__ = ["generate_encounters"]

class Monster(object):
    def __init__(self):
        self.hp = 10
        self.pw = 2

class Item(object):
    def __init__(self):
        self.name = ""
        self.desc = ""
        self.stackSize = 1
        self.consumable = False
        self.statTable = {}

def generate_encounters(turns):
    """ Return a queue of (Monster, Item) pairs of length TURNS."""
    encounters = queue.Queue()
    for i in range(turns):
        encounters.put(None) # Generate new monsters and items

    return encounters


def new_monster(): pass
def new_item(): pass
