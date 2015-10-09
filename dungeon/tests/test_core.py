# coding=utf-8
# Dungeon -> Tests -> Core

import pytest
import dungeon.main as main
import dungeon.stats.generate as gen

class TestNewRoom:
    def test_return(s):
        char = gen.monster()
        accs = gen.accessory()
        mons = gen.monster()
