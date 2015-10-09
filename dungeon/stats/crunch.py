# coding=utf-8
# Dungeon -> Stats -> Crunch

# Untested
def chance(n):
    return random.uniform(0, 1) < n


def tweak(n, low=0.6, high=1.4):
    return n * random.uniform(low, high)


def damage(character, monster, chance=True):
    """Simulate an attack on the character by a monster.
    Return the modified copy of character. (no mutation)
    """

    char = character.copy()
    loss = monster['PW'] - char['DF']
    if chance:
        loss = tweak(loss)
        if chance(0.2):  # Critical hit
            loss = tweak(loss, 1.2, 2.4)
    if loss < 1: 
        loss = 1

    char['HP'] -= loss
    if char['HP'] < 0:
        char['HP'] = 0
    return char


def first(character, monster, chance=True):
    """Return True if the character moves first, otherwise False."""
    
    charSp = character['SP']
    monsSp = monster['SP']
    if chance:
        charSp = tweak(charSp)
        monsSp = tweak(monsSp)
    return charSp >= monsSp


# XXX
def old_damage(defender, attacker):
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
