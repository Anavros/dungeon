#!/usr/bin/python3

import sys; sys.dont_write_bytecode = True

from enum import Enum

import item
import monster
import character

class Materials(Enum):
    Iron, Copper, Adamantine = range(3)

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

"""
    Inventory: Dictionary
        -> Item Shield *TBA
        -> Item Left Hand
        -> Item Right Hand
        -> Item Armor
        -> List [Item] Bag
        -> (why not toss char stats in here if there's only one)
        -> Int HP
        -> Int Power
        -> String Name
        -> Int Level *TBA
        -> Int Big Bucks *TBA

    Item: Tuple
        -> String Name
        -> String Description
        -> Int Stack Size
        -> Bool Consumable
        -> Stat Table (merge with player's)
        -> Attribute Table (only used in creation?)
    (Consider splitting items into armor, weapons, and consumables)
"""
