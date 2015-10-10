# coding=utf-8
# Dungeon -> Stats -> Crunch

import random

# Untested (no need)
def chance(n):
    return random.uniform(0, 1) < n


# Untested (no need) ((will inevitable come back to bite me in the ass))
def tweak(n, low=0.6, high=1.4):
    return int(n * random.uniform(low, high))


# Tested
def damage(character, monster, rand=True):
    """Simulate an attack on the character by a monster.
    Return the modified copy of character. (no mutation)
    """

    char = character.copy()
    loss = monster['PW'] - char['DF']
    if rand:
        loss = tweak(loss)
        if chance(0.2):  # Critical hit
            loss = tweak(loss, 1.2, 2.4)
    if loss < 1: 
        loss = 1

    char['HP'] -= loss
    if char['HP'] < 0:
        char['HP'] = 0
    return char


# Tested
def first_moves_first(character, monster, rand=True):
    """Return True if the character moves first, otherwise False."""
    
    c_sp = character['SP']
    m_sp = monster['SP']
    if rand:
        c_sp = tweak(c_sp)
        m_sp = tweak(m_sp)
    return c_sp >= m_sp
