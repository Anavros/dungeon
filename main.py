#!/usr/bin/python3
# Dungeon -> Main

import sys; sys.dont_write_bytecode = True

import game
import interface
# Python 3 module import behavior testing
import modules

print(modules.my_func())

print("+++Welcome to the Dungeon+++")
while True:
    print("\nMain Menu")
    keyword = interface.get_command(['NEW', 'EXIT'])
    if keyword == 'NEW':
        # TODO Include better character creation
        print("Enter your name: ", end="")
        name = interface.get_free_input()

        victory = game.start_new_game(name)
        if victory:
            print("You won! Congratulations %s!" % name)
        else:
            print("You are dead.")
        interface.wait_for_input()

    elif keyword == 'EXIT':
        break
