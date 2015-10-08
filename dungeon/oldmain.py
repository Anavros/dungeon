#!/usr/bin/python3
# coding=utf-8

# Dungeon -> Main
import yaml
import interface as interface
import tools as tools
import stats as stats

TURNS = 5
CONFIG = None
with open('dungeon/config.yml', 'r') as CONFIG_FILE:
    CONFIG = yaml.load(CONFIG_FILE)

def config():
    """Take the data found in config.yml and send it to the tools module."""
    tools.monsterSet = CONFIG['monsters']

def main():
    print("+++Welcome to the Dungeon+++")
    if CONFIG is not None:
        config()
    while True:
        print("\nMain Menu")
        keyword = interface.get_command(['NEW', 'CONFIG', 'EXIT'])
        if keyword.upper() == 'NEW':
            victory = start_new_game()
            if victory:
                print("You won! Congratulations!")
            else:
                print("You are dead.")
            interface.wait_for_input()

        elif keyword.upper() == 'CONFIG':
            print(CONFIG)

        elif keyword.upper() == 'EXIT':
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
    mons = monster.copy()
    print("You come face-to-face with {}!".format(monster))
    while True:
        (char, loss, crit) = stats.damage(char, mons)
        print("It lunges towards you!")
        if crit: print("The attack catches you by surprise!")
        print("You take {} damage!".format(loss))
        print("What will you do?")

        keyword = interface.get_command(['ATTACK', 'WAIT', 'LOOK', 'RETIRE'])
        if keyword.upper() == 'ATTACK':
            (mons, loss, crit) = stats.damage(mons, char)
            if crit: print("You execute your attack with deft precision!")
            print("You attack the monster, dealing {} damage!".format(loss))
        elif keyword.upper() == 'WAIT':
            print("You do nothing.")
        elif keyword.upper() == 'LOOK':
            print("You examine the monster.")
            print("Is is {}.".format(mons.desc))
            print("It has {} HP left.".format(mons.stats['HP']))
        elif keyword.upper() == 'RETIRE':
            char = retire(char)
        else:
            assert False, "We've made a mistake!"

        interface.wait_for_input()

        if not mons.is_alive():
            print("You have defeated the monster!")
            break
        if not char.is_alive():
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
