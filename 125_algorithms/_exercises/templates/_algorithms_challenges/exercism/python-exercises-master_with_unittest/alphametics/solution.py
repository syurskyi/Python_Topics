____ i.. _______ combinations, permutations


___ check_leading_zeros(*numbers):
    r.. any(n[0] __ '0' ___ n __ numbers)


___ test_equation(puzzle, substitutions):
    equation = ''.j..(substitutions.get(char) o. char ___ char __ puzzle)
    left, right = equation.s..(' == ')
    left_numbers = left.s..(' + ')

    __ check_leading_zeros(right, *left_numbers):
        r.. F..

    r.. s..(map(i.., left_numbers)) __ i..(right)


___ solve(puzzle):
    letters = s..(char ___ char __ puzzle __ char.isupper())
    numbers = map(s.., r..(10))

    ___ c __ combinations(numbers, l..(letters)):
        ___ p __ permutations(c):
            substitutions = d..(z..(letters, p))
            __ test_equation(puzzle, substitutions):
                r.. {k: i..(v) ___ k, v __ substitutions.i..}

    r.. {}  # no solution found
