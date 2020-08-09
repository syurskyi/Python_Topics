from itertools ______ permutations

___ solution(
    """Finds solutions to the zebra puzzle"""
    solutions = list(zebra_puzzle())
    assert(le.(solutions) __ 1)
    r_ ("It is the %s who drinks the water.\n"
        "The %s keeps the zebra." %(solutions[0]['water'], solutions[0]['zebra']))

___ zebra_puzzle(
    """Iterator that finds all solutions to the zebra puzzle"""
    residents = 'Englishman, Spaniard, Ukranian, Japanese, Norwegian'.split(', ')
    orderings = list(permutations(residents))
    first, _, middle, _, _ = (0, 1, 2, 3, 4)

    ___ (red, green, ivory, yellow, blue) in orderings:
        __ red != 'Englishman':
            continue
        ___ order in orderings:
            __ abs(order.index('Norwegian') - order.index(blue)) != 1:
                continue
            __ order[0] != 'Norwegian':
                continue
            __ order.index(green) - order.index(ivory) != 1:
                continue
            ___ (dog, snails, fox, horse, ZEBRA) in orderings:
                __ dog != 'Spaniard':
                    continue
                ___ (coffee, tea, milk, oj, WATER) in orderings:
                    __ order.index(milk) != middle:
                        continue
                    __ coffee != green:
                        continue
                    __ tea != 'Ukranian':
                        continue
                    ___ (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings:
                        __ OldGold != snails:
                            continue
                        __ Kools != yellow:
                            continue
                        __ abs(order.index(Chesterfields) - order.index(fox)) != 1:
                            continue
                        __ abs(order.index(Kools) - order.index(horse)) != 1:
                            continue
                        __ LuckyStrike != oj:
                            continue
                        __ Parliaments != 'Japanese':
                            continue
                        yield { 'zebra': ZEBRA, 'water': WATER }

