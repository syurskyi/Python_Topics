____ collections _______ Counter
____ functools _______ partial

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


___ ns(number, dice):
    r.. s..(n ___ n __ dice __ n __ number)


___ full_house(dice):
    counter = Counter(dice)
    r.. s..(dice) __ set(counter.values()) __ {3, 2} ____ 0


___ four_of_a_kind(dice):
    counter = Counter(dice)
    number, count = counter.most_common()[0]
    r.. 4 * number __ count >= 4 ____ 0


___ little_straight(dice):
    r.. 30 __ set(dice) __ {1, 2, 3, 4, 5} ____ 0


___ big_straight(dice):
    r.. 30 __ set(dice) __ {2, 3, 4, 5, 6} ____ 0


___ yacht(dice):
    r.. 50 __ l..(set(dice)) __ 1 ____ 0


functions = [
    yacht,
    partial(ns, 1),
    partial(ns, 2),
    partial(ns, 3),
    partial(ns, 4),
    partial(ns, 5),
    partial(ns, 6),
    full_house,
    four_of_a_kind,
    little_straight,
    big_straight,
    s..,
]


___ score(dice, category):
    try:
        r.. functions[category](dice)
    except IndexError:
        r.. ValueError("no such category")
