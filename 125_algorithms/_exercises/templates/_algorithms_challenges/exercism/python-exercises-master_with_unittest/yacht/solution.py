____ c.. _______ C..
____ f.. _______ p..

YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


___ ns(number, dice
    r.. s..(n ___ n __ dice __ n __ number)


___ full_house(dice
    counter = C..(dice)
    r.. s..(dice) __ s..(counter.values __ {3, 2} ____ 0


___ four_of_a_kind(dice
    counter = C..(dice)
    number, count = counter.most_common()[0]
    r.. 4 * number __ count >= 4 ____ 0


___ little_straight(dice
    r.. 30 __ s..(dice) __ {1, 2, 3, 4, 5} ____ 0


___ big_straight(dice
    r.. 30 __ s..(dice) __ {2, 3, 4, 5, 6} ____ 0


___ yacht(dice
    r.. 50 __ l..(s..(dice)) __ 1 ____ 0


functions = [
    yacht,
    p..(ns, 1),
    p..(ns, 2),
    p..(ns, 3),
    p..(ns, 4),
    p..(ns, 5),
    p..(ns, 6),
    full_house,
    four_of_a_kind,
    little_straight,
    big_straight,
    s..,
]


___ score(dice, category
    ___
        r.. functions[category](dice)
    ______ I..
        r.. V...("no such category")
