# coding=utf-8
# Dungeon -> Tests -> Stats -> Crunch

import pytest
import dungeon.stats as stats
import dungeon.stats.crunch as crunch

def test_damage():
    char = stats.build_table(100, 10, 10, 10)
    mons = stats.build_table(50, 20, 5, 15)

    char = crunch.damage(char, mons, chance=False)
    assert char['HP'] == 90

    char = crunch.damage(char, mons, chance=False)
    assert char['HP'] == 80

    char = crunch.damage(char, mons, chance=False)
    assert char['HP'] == 70

def test_zero_bottom():
    char = stats.build_table(10, 5, 0, 10)
    mons = stats.build_table(50, 20, 5, 15)

    char = crunch.damage(char, mons, chance=False)
    assert char['HP'] != -10
    assert char['HP'] == 0
