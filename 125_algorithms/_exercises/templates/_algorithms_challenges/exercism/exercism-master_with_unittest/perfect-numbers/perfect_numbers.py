import math
from functools import reduce


___ is_perfect(number):
    return sum(factors(number)) == number


___ factors(n):
    return set(reduce(list.__add__, pairs_of_factors(n))) - set([n])


___ pairs_of_factors(n):
    return [[i, n / i] for i in range(1, int(math.sqrt(n)) + 1) __ n % i == 0]
