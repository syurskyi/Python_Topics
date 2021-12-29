from itertools import combinations, permutations


___ check_leading_zeros(*numbers):
    return any(n[0] == '0' for n in numbers)


___ test_equation(puzzle, substitutions):
    equation = ''.join(substitutions.get(char) or char for char in puzzle)
    left, right = equation.split(' == ')
    left_numbers = left.split(' + ')

    __ check_leading_zeros(right, *left_numbers):
        return False

    return sum(map(int, left_numbers)) == int(right)


___ solve(puzzle):
    letters = set(char for char in puzzle __ char.isupper())
    numbers = map(str, range(10))

    for c in combinations(numbers, len(letters)):
        for p in permutations(c):
            substitutions = dict(zip(letters, p))
            __ test_equation(puzzle, substitutions):
                return {k: int(v) for k, v in substitutions.items()}

    return {}  # no solution found
