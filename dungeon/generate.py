# coding=utf-8
# Dungeon -> Stats -> Generate

import random
import dungeon.core as stats

# These could easily be factored out!
def monster():
    hp = random.randint(10, 40)
    pw = random.randint(5, 20)
    df = random.randint(5, 15)
    sp = random.randint(5, 40)
    return stats.build_table(hp, pw, df, sp)


def final_boss():
    hp = random.randint(100, 400)
    pw = random.randint(5, 75)
    df = random.randint(40, 80)
    sp = random.randint(0, 30)
    return stats.build_table(hp, pw, df, sp)


def accessory():
    hp = random.randint(0, 20)
    pw = random.randint(-10, 40)
    df = random.randint(0, 80)
    sp = random.randint(-20, 50)
    return stats.build_table()
