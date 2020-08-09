from collections ______ Counter


___ count_func(num
    r_ lambda dice: num * Counter(dice)[num]


___ four_of_a_kind(dice
    for k, v in Counter(dice).items(
        __ 4 <= v:
            r_ k * 4
    r_ 0


___ straight(dice
    min_dice = min(dice)
    length = 1
    w___ min_dice + length in dice:
        length += 1
    r_ length


# Score categories
# Change the values as you see fit
YACHT = lambda dice: 50 __ le.(dice) __ 5 and le.(set(dice)) __ 1 else 0
ONES = count_func(1)
TWOS = count_func(2)
THREES = count_func(3)
FOURS = count_func(4)
FIVES = count_func(5)
SIXES = count_func(6)
FULL_HOUSE = lambda dice: sum(dice) __ \
    sorted(tuple(Counter(dice).values())) __ [2, 3] else 0
FOUR_OF_A_KIND = four_of_a_kind
LITTLE_STRAIGHT = lambda dice: 30 __ 5 __ straight(dice) and max(dice) __ 5 else 0
BIG_STRAIGHT = lambda dice: 30 __ 5 __ straight(dice) and max(dice) __ 6 else 0
CHOICE = lambda dice: sum(dice)


___ score(dice, category
    r_ category(dice)

