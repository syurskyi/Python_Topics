#!/usr/bin/env python3

"""
sequential.py: baseline for comparing sequential, multiprocessing,
and threading code for CPU-intensive work.
"""

____ t__ ______ perf_counter
____ typing ______ NamedTuple

____ primes ______ is_prime, NUMBERS

c_ Result(NamedTuple):  # <1>
    prime: bool
    elapsed: float

___ check(n: in.)  Result:  # <2>
    t0 = perf_counter()
    prime = is_prime(n)
    r_ Result(prime, perf_counter() - t0)

___ main()  N..:
    print(f'Checking {l..(NUMBERS)} numbers sequentially:')
    t0 = perf_counter()
    ___ n __ NUMBERS:  # <3>
        prime, elapsed = check(n)
        label = 'P' __ prime else ' '
        print(f'{n:16}  {label} {elapsed:9.6f}s')

    elapsed = perf_counter() - t0  # <4>
    print(f'Total time: {elapsed:.2f}s')

__ _____ __ ______
    main()
