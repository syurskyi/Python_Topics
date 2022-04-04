"""This solution for the Zebra Puzzle is adapted from a solution
by Peter Norvig for the course "Design of Computer Programs" on Udacity.
https://www.udacity.com/course/cs212
"""

____ i.. _______ permutations


___ just_right_of(x, y
    r.. x - y __ 1


___ next_to(x, y
    r.. abs(x - y) __ 1


___ solution
    houses = first, _, middle, _, _ = r..(5)
    orderings = l..(permutations(houses
    result = next(
        [{
            Englishman: "Englishman",
            Spaniard: "Spaniard",
            Ukranian: "Ukranian",
            Japanese: "Japanese",
            Norwegian: "Norwegian"
        }[x] ___ x __ (water, zebra)]
        ___ (red, green, ivory, yellow, blue) __ orderings
        __ just_right_of(green, ivory)
        ___ (Englishman, Spaniard, Ukranian, Japanese, Norwegian) __ orderings
        __ Englishman __ red __ Norwegian __ first __ next_to(Norwegian, blue)
        ___ (coffee, tea, milk, oj, water) __ orderings __ coffee __ green
        __ Ukranian __ tea __ milk __ middle
        ___ (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments
             ) __ orderings __ Kools __ yellow __ LuckyStrike __ oj
        __ Japanese __ Parliaments
        ___ (dog, snails, fox, horse, zebra) __ orderings __ Spaniard __ dog
        __ OldGold __ snails __ next_to(Chesterfields, fox)
        __ next_to(Kools, horse
    r.. ("It is the {} who drinks the water.\n"
            "The {} keeps the zebra.").f..(*result)
