#!/usr/bin/python3
# coding=utf-8

# Dungeon -> Main

import sys; sys.dont_write_bytecode = True
import copy

import interface
import tools
import stats

TURNS = 5

def main():
    print("+++Welcome to the Dungeon+++")
    while True:
        print("\nMain Menu")
        keyword = interface.get_command(['NEW', 'EXIT'])
        if keyword == 'NEW':
            victory = start_new_game()
            if victory:
                print("You won! Congratulations!")
            else:
                print("You are dead.")
            interface.wait_for_input()

        elif keyword == 'EXIT':
            break


def examine_loot(item): 
    print("You found {}!".format(item))


def retire(character):
    """Set the character's HP to 0 and return a copy. Return a copy of character."""

    char = character.copy()
    print("You get the heck out of that dungeon as soon as possible.")
    print("However, you trip on an unseen wire near the entrance!")
    print("You fall into a pit of terrible monsters.")
    print("There is no escaping from the dungeon.")
    char.stats['HP'] = 0
    return char


def fight(character, monster):
    """Pit the character against a monster until one or both are dead.
    Return a copy of character."""

    char = character.copy()
    print("You come face-to-face with {}!".format(monster))
    while True:
        print("It lunges towards you!")
        pw = monster.stats['PW']
        print("You take {} damage!".format(pw))
        char.stats['HP'] -= pw

        print("What will you do?")
        keyword = interface.get_command(['ATTACK', 'WAIT', 'RETIRE'])
        if keyword.upper() == 'ATTACK':
            pw = char.stats['PW']
            print("You attack the monster, dealing {} damage!".format(pw))
            monster.stats['HP'] -= pw
        elif keyword.upper() == 'WAIT':
            print("You do nothing.")
        elif keyword.upper() == 'RETIRE':
            char = retire(char)
        else:
            assert False, "We've made a mistake!"

        interface.wait_for_input()

        if monster.stats['HP'] < 1:
            print("You have defeated the monster!")
            break
        if char.stats['HP'] < 1:
            break
    return char


def present_encounter(character, encounter):
    """Offer the character a chance to fight a monster. Return a copy of character."""

    char = character.copy()
    (monster, item) = encounter
    print("Do you wish to fight a monster?")
    keyword = interface.get_command(['YES', 'NO'])
    if keyword.upper() == 'YES':
        char = fight(char, monster)
    elif keyword.upper() == 'NO':
        print("You slink past the monster unharmed.")

    if char.is_alive():
        examine_loot(item)
    return char
    

def start_new_game():
    """Start a new round. Return True for a win or False for a loss."""

    character = tools.generate_character()
    encounters = tools.generate_encounters(TURNS)

    print("You wander into an old, decrepit dungeon...\n")

    for encounter in encounters:
        print("What will you do?")
        interface.print_stat_table(character.stats)
        keyword = interface.get_command(['EXPLORE', 'RETIRE'])
        if keyword.upper() == 'EXPLORE':
            character = present_encounter(character, encounter)
        elif keyword.upper() == 'RETIRE':
            character = retire(character)
            interface.wait_for_input()
        
        if not character.is_alive():
            return False

    return True

if __name__ == '__main__': main()
