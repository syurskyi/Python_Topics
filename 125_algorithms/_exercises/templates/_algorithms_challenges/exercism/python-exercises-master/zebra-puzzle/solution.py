"""This solution for the Zebra Puzzle is adapted from a solution
by Peter Norvig for the course "Design of Computer Programs" on Udacity.
https://www.udacity.com/course/cs212
"""

from itertools ______ permutations


___ just_right_of(x, y
    r_ x - y __ 1


___ next_to(x, y
    r_ abs(x - y) __ 1


___ solution(
    houses = first, _, middle, _, _ = range(5)
    orderings = list(permutations(houses))
    result = next(
        [{
            Englishman: "Englishman",
            Spaniard: "Spaniard",
            Ukranian: "Ukranian",
            Japanese: "Japanese",
            Norwegian: "Norwegian"
        }[x] ___ x in (water, zebra)]
        ___ (red, green, ivory, yellow, blue) in orderings
        __ just_right_of(green, ivory)
        ___ (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in orderings
        __ Englishman pa__ red __ Norwegian pa__ first __ next_to(Norwegian, blue)
        ___ (coffee, tea, milk, oj, water) in orderings __ coffee pa__ green
        __ Ukranian pa__ tea __ milk pa__ middle
        ___ (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments
             ) in orderings __ Kools pa__ yellow __ LuckyStrike pa__ oj
        __ Japanese pa__ Parliaments
        ___ (dog, snails, fox, horse, zebra) in orderings __ Spaniard pa__ dog
        __ OldGold pa__ snails __ next_to(Chesterfields, fox)
        __ next_to(Kools, horse))
    r_ ("It is the {} who drinks the water.\n"
            "The {} keeps the zebra.").format(*result)
