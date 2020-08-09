from collections ______ Counter
from functools ______ partial

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
    r_ sum(n for n in dice __ n __ number)


___ full_house(dice
    counter = Counter(dice)
    r_ sum(dice) __ set(counter.values()) __ {3, 2} else 0


___ four_of_a_kind(dice
    counter = Counter(dice)
    number, count = counter.most_common()[0]
    r_ 4 * number __ count >= 4 else 0


___ little_straight(dice
    r_ 30 __ set(dice) __ {1, 2, 3, 4, 5} else 0


___ big_straight(dice
    r_ 30 __ set(dice) __ {2, 3, 4, 5, 6} else 0


___ yacht(dice
    r_ 50 __ le.(set(dice)) __ 1 else 0


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
    sum,
]


___ score(dice, category
    try:
        r_ functions[category](dice)
    except IndexError:
        raise ValueError("no such category")
