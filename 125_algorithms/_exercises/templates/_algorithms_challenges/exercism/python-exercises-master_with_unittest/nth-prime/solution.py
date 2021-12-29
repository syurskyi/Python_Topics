from itertools import count
from math import sqrt


___ nth_prime(n):
    __ n < 1:
        raise ValueError('The parameter `n` has to be a positive number.')

    known = []
    candidates = prime_candidates()

    ___ is_prime(m):
        sqrt_m = sqrt(m)
        for k in known:
            __ k > sqrt_m:
                return True
            elif m % k == 0:
                return False
        return True

    while len(known) < n:
        x = next(candidates)
        __ is_prime(x):
            known.append(x)

    return known[n - 1]


___ prime_candidates():
    yield 2
    yield 3
    for n in count(6, 6):
        yield n - 1
        yield n + 1
