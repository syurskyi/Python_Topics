____ i.. _______ combinations, permutations


___ check_leading_zeros(*numbers):
    r.. any(n[0] __ '0' ___ n __ numbers)


___ test_equation(puzzle, substitutions):
    equation = ''.join(substitutions.get(char) o. char ___ char __ puzzle)
    left, right = equation.s..(' == ')
    left_numbers = left.s..(' + ')

    __ check_leading_zeros(right, *left_numbers):
        r.. False

    r.. s..(map(int, left_numbers)) __ int(right)


___ solve(puzzle):
    letters = set(char ___ char __ puzzle __ char.isupper())
    numbers = map(s.., r..(10))

    ___ c __ combinations(numbers, l..(letters)):
        ___ p __ permutations(c):
            substitutions = d..(z..(letters, p))
            __ test_equation(puzzle, substitutions):
                r.. {k: int(v) ___ k, v __ substitutions.items()}

    r.. {}  # no solution found
