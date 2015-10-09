# coding=utf-8
# Dungeon -> Stats

import random

def build_table(hp=0, pw=0, df=0, sp=0):
    """Return a dictionary where HP, PW, DF, and SP are mapped to ints.
    Keyword arguments can be used to change the values (default to 0). This 
    is the standard format for stat tables used throughout the program.
    """
    rawTable = {
        "HP": hp,
        "PW": pw,
        "DF": df,
        "SP": sp}

    safeTable = {}
    for (k, v) in rawTable.items():  # New in py3k?
        if type(v) is not int:
            try:
                v = int(v)
            except ValueError:
                v = 0
        
        # Should always be an integer at this point
        safeTable[k] = int(v)
    return safeTable


def extract(stats):
    """Return HP, PW, DF, and SP as a tuple from a given stat table.
    (shortcut method) Does not modify input.
    """
    return (stats['HP'], stats['PW'], stats['DF'], stats['SP']) 


def stack(*tables):
    """Add all stats together from given tables.
    Used for combining armor, potion effects, etc. with characters' base stats.
    If totals are negative, they are set to 0.
    Returns a new stat table.
    """
    stats = build_table()
    for table in tables:
        stats['HP'] += table['HP']
        stats['PW'] += table['PW']
        stats['DF'] += table['DF']
        stats['SP'] += table['SP']
    if stats['HP'] <= 0: stats['HP'] = 0
    if stats['PW'] <= 0: stats['PW'] = 0
    if stats['DF'] <= 0: stats['DF'] = 0
    if stats['SP'] <= 0: stats['SP'] = 0
    return stats


# Untested
def output_table(table, outFn=print):
    """Displays a string containing a given table's values."""

    outFn("HP: {} | PW: {} | DF: {} | SP: {}".format(extract(table)))


# Untested
#def damage(defender, attacker):
#    """Take HP from the first table according to the second table's PW.
#    Also takes defence and other factors into consideration.
#    Return a copy of defender and the total amount lost as a tuple."""
#
#    (d_hp, d_pw, d_df, d_sp) = extract(defender.stats)
#    (a_hp, a_pw, a_df, a_sp) = extract(attacker.stats)
#
#    crit = random.uniform(0, 1) < 0.2
#    loss = a_pw - d_df
#    loss = int(loss*random.uniform(0.8, 1.2))
#    if crit: loss *= 2
#    if loss < 1: loss = 1
#    d_hp -= loss
#
#    defender.stats = build_table(d_hp, d_pw, d_df, d_sp)
#    return (defender, loss, crit)
