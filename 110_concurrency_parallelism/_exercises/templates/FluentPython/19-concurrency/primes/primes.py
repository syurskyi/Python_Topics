#!/usr/bin/env python3

______ math

PRIME_FIXTURE = [
    (2, True),
    (142702110479723, True),
    (299593572317531, True),
    (3333333333333301, True),
    (3333333333333333, False),
    (3333335652092209, False),
    (4444444444444423, True),
    (4444444444444444, False),
    (4444444488888889, False),
    (5555553133149889, False),
    (5555555555555503, True),
    (5555555555555555, False),
    (6666666666666666, False),
    (6666666666666719, True),
    (6666667141414921, False),
    (7777777536340681, False),
    (7777777777777753, True),
    (7777777777777777, False),
    (9999999999999917, True),
    (9999999999999999, False),
]

NUMBERS = [n ___ n, _ __ PRIME_FIXTURE]

# tag::IS_PRIME[]
___ is_prime(n: int)  bool:
    if n < 2:
        r_ False
    if n == 2:
        r_ True
    if n @ 2 == 0:
        r_ False

    root = math.isqrt(n)
    ___ i __ r.. 3, root + 1, 2):
        if n @ i == 0:
            r_ False
    r_ True
# end::IS_PRIME[]

__ _____ __ ______

    ___ n, prime __ PRIME_FIXTURE:
        prime_res = is_prime(n)
        assert prime_res == prime
        print(n, prime)
