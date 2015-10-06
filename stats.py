# coding=utf-8
# Dungeon -> Stats

import random

def build_table(hp=0, pw=0, df=0, sp=0):
    return {
        "HP": hp,
        "PW": pw,
        "DF": df,
        "SP": sp}


def extract(stats):
    """Return HP, PW, DF, and SP as a tuple from a given stat table.
    (shortcut method) Does not modify inputs.
    """
    return (stats['HP'], stats['PW'], stats['DF'], stats['SP']) 


def damage(defender, attacker):
    """Take HP from the first table according to the second table's PW.
    Also takes defence and other factors into consideration.
    Return a copy of defender and the total amount lost as a tuple."""

    (d_hp, d_pw, d_df, d_sp) = extract(defender.stats)
    (a_hp, a_pw, a_df, a_sp) = extract(attacker.stats)

    crit = random.uniform(0, 1) < 0.2
    loss = a_pw - d_df
    loss = int(loss*random.uniform(0.8, 1.2))
    if crit: loss *= 2
    if loss < 1: loss = 1
    d_hp -= loss

    defender.stats = build_table(d_hp, d_pw, d_df, d_sp)
    return (defender, loss, crit)


# Could prevent <0 values?
def stack(tables):
    """Add all stats together from a list of tables.
    Used for combining armor, potion effects, etc. with characters' base stats.
    Returns a new stat table.
    """
    stats = build_table()
    for table in tables:
        stats['HP'] += table['HP']
        stats['PW'] += table['PW']
        stats['DF'] += table['DF']
        stats['SP'] += table['SP']
    return stats
