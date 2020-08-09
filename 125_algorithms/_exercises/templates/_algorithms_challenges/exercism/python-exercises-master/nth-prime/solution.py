from itertools ______ count
from ma__ ______ sqrt


___ nth_prime(n
    __ n < 1:
        raise ValueError('The parameter `n` has to be a positive number.')

    known = []
    candidates = prime_candidates()

    ___ is_prime(m
        sqrt_m = sqrt(m)
        ___ k in known:
            __ k > sqrt_m:
                r_ True
            ____ m % k __ 0:
                r_ False
        r_ True

    w___ le.(known) < n:
        x = next(candidates)
        __ is_prime(x
            known.append(x)

    r_ known[n - 1]


___ prime_candidates(
    yield 2
    yield 3
    ___ n in count(6, 6
        yield n - 1
        yield n + 1
