____ i.. _______ count
____ math _______ sqrt


___ nth_prime(n):
    __ n < 1:
        r.. ValueError('The parameter `n` has to be a positive number.')

    known    # list
    candidates = prime_candidates()

    ___ is_prime(m):
        sqrt_m = sqrt(m)
        ___ k __ known:
            __ k > sqrt_m:
                r.. T..
            ____ m % k __ 0:
                r.. F..
        r.. T..

    w.... l..(known) < n:
        x = next(candidates)
        __ is_prime(x):
            known.a..(x)

    r.. known[n - 1]


___ prime_candidates
    y.. 2
    y.. 3
    ___ n __ c.. 6, 6):
        y.. n - 1
        y.. n + 1
