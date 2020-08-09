from itertools ______ combinations, permutations


___ check_leading_zeros(*numbers
    r_ any(n[0] __ '0' ___ n in numbers)


___ test_equation(puzzle, substitutions
    equation = ''.join(substitutions.get(char) or char ___ char in puzzle)
    left, right = equation.split(' == ')
    left_numbers = left.split(' + ')

    __ check_leading_zeros(right, *left_numbers
        r_ False

    r_ su.(map(int, left_numbers)) __ int(right)


___ solve(puzzle
    letters = set(char ___ char in puzzle __ char.isupper())
    numbers = map(str, range(10))

    ___ c in combinations(numbers, le.(letters)):
        ___ p in permutations(c
            substitutions = dict(zip(letters, p))
            __ test_equation(puzzle, substitutions
                r_ {k: int(v) ___ k, v in substitutions.items()}

    r_ {}  # no solution found
