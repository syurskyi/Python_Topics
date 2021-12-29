____ itertools _______ count
____ math _______ sqrt


___ nth_prime(n):
    __ n < 1:
        raise ValueError('The parameter `n` has to be a positive number.')

    known    # list
    candidates = prime_candidates()

    ___ is_prime(m):
        sqrt_m = sqrt(m)
        ___ k __ known:
            __ k > sqrt_m:
                r.. True
            ____ m % k __ 0:
                r.. False
        r.. True

    while l..(known) < n:
        x = next(candidates)
        __ is_prime(x):
            known.a..(x)

    r.. known[n - 1]


___ prime_candidates():
    yield 2
    yield 3
    ___ n __ c.. 6, 6):
        yield n - 1
        yield n + 1
