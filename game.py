# Dungeon -> Game

import tools
import stats
import interface

TURNS = 10

def fight_monster(): pass


def examine_loot(): 
    print("Ooo! Shiny loot!")


def retire(character):
    print("You get the heck out of that dungeon as soon as possible.")
    print("However, you trip on an unseen wire near the entrance!")
    print("You fall into a pit of terrible monsters.")
    print("There is no escaping from the dungeon.")
    character['HP'] = 0
    return character


def present_encounter(monster, item, character):
    print("You come face-to-face with %s!" % monster)
    while True:
        print("It lunges towards you!")
        pw = monster.stats['PW']
        print("You take %s damage!" % pw)
        character['HP'] -= pw

        print("What will you do?")
        keyword = interface.get_command(['ATTACK', 'WAIT', 'RETIRE'])
        if keyword.upper() == 'ATTACK':
            pw = character['PW']
            print("You attack the monster, dealing %s damage!" % pw)
            monster.stats['HP'] -= pw
        elif keyword.upper() == 'WAIT':
            print("You do nothing.")
        elif keyword.upper() == 'RETIRE':
            character = retire(character)
        else:
            assert False, "We've made a mistake!"

        interface.wait_for_input()

        if monster.stats['HP'] < 1:
            print("You have defeated the monster!")
            break
        if character['HP'] < 1:
            break
    return character
    

def start_new_game(name):
    victory = False
    heldItem = None
    character = stats.build_table(hp=100, pw=20, df=10, sp=20)
    encounters = tools.generate_encounters(TURNS)

    print("You wander into an old, decrepit dungeon...\n")

    while not encounters.empty():
        (monster, item) = encounters.get()
        print("What will you do?")
        interface.print_stat_table(character)
        keyword = interface.get_command(['EXPLORE', 'RETIRE'])
        if keyword.upper() == 'EXPLORE':
            character = present_encounter(monster, item, character)
        elif keyword.upper() == 'RETIRE':
            character = retire(character)
            interface.wait_for_input()

        if character['HP'] > 0:
            examine_loot()
        else:
            victory = False
            break
        interface.wait_for_input()

    if character['HP'] < 1:
        return False
    # Needs to be moved to new sub
    boss = tools.generate_final_boss()
    treasure = tools.generate_treasure()
    present_encounter(boss, treasure, character)
    if character['HP'] > 0:
        print("You have conquered the dungeon!")
        victory = True
    else:
        victory = False
    return victory
