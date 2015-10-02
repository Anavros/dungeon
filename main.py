#!/usr/bin/python3

# Dungeon
# A moderately complex RPG
# Now using Python 3!

import sys; sys.dont_write_bytecode = True

import queue

import encounter

# Constants
STAT_POOL = 20
TURNS = 10 # Temporary until keys are added

# Flags
PLAYER_WON = False

# Generate list of encounters
# encounters is a queue, so use e.get(), watch out for e.Empty exception
encounters = tools.generate_encounters(TURNS)

# Add keys to certain encounters?
# For now have a set number of turns

# Generate final boss
finalBoss = None

# Create a new character
# Allowing the user to customize them
# Name, and allocating stats from a pool

while True:
    # Present encounter
    """
    try:
        #(monster, item) = encounters.get()
        encounters.get()
    except queue.Empty as e:
        print("There are no more encounters!")
        break
    """
    if encounters.empty():
        break
    else:
        print(encounters.get())

    # Review turn   
    input()

if PLAYER_WON:
    print("You won! Congratulations!")
else:
    print("You lost! Deal with it~")


"""
    Generate list of encounters so that:
        -Each key appears once
        -Each encounter has Items/Monsters for loot and explore *Could be simplified
    Generate final boss
    Create a new character and empty inventory
    Loop until character dies:
        Choose path
            -> if loot, hard items/monsters
            -> if explore, easy ones
        Present encounter
            -> Fight all monsters
            -> Give all items
        Review
        Start next turn
        
        **Special case: If player has all keys
        Present final boss
            -if win: set won flag and break
            -if lose, progress normally, player hp == 0 -> lose
    Congratulate / Tease player for winning or losing
    Back to main menu
"""
