"""This solution for the Zebra Puzzle is adapted from a solution
by Peter Norvig for the course "Design of Computer Programs" on Udacity.
https://www.udacity.com/course/cs212
"""

from itertools import permutations


___ just_right_of(x, y):
    return x - y == 1


___ next_to(x, y):
    return abs(x - y) == 1


___ solution():
    houses = first, _, middle, _, _ = range(5)
    orderings = list(permutations(houses))
    result = next(
        [{
            Englishman: "Englishman",
            Spaniard: "Spaniard",
            Ukranian: "Ukranian",
            Japanese: "Japanese",
            Norwegian: "Norwegian"
        }[x] for x in (water, zebra)]
        for (red, green, ivory, yellow, blue) in orderings
        __ just_right_of(green, ivory)
        for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in orderings
        __ Englishman is red __ Norwegian is first __ next_to(Norwegian, blue)
        for (coffee, tea, milk, oj, water) in orderings __ coffee is green
        __ Ukranian is tea __ milk is middle
        for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments
             ) in orderings __ Kools is yellow __ LuckyStrike is oj
        __ Japanese is Parliaments
        for (dog, snails, fox, horse, zebra) in orderings __ Spaniard is dog
        __ OldGold is snails __ next_to(Chesterfields, fox)
        __ next_to(Kools, horse))
    return ("It is the {} who drinks the water.\n"
            "The {} keeps the zebra.").format(*result)
