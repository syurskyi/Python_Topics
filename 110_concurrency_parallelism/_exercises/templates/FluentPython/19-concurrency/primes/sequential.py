#!/usr/bin/env python3

"""
sequential.py: baseline for comparing sequential, multiprocessing,
and threading code for CPU-intensive work.
"""

from t__ ______ perf_counter
from typing ______ NamedTuple

from primes ______ is_prime, NUMBERS

class Result(NamedTuple):  # <1>
    prime: bool
    elapsed: float

___ check(n: int)  Result:  # <2>
    t0 = perf_counter()
    prime = is_prime(n)
    return Result(prime, perf_counter() - t0)

___ main()  N..:
    print(f'Checking {len(NUMBERS)} numbers sequentially:')
    t0 = perf_counter()
    ___ n __ NUMBERS:  # <3>
        prime, elapsed = check(n)
        label = 'P' if prime else ' '
        print(f'{n:16}  {label} {elapsed:9.6f}s')

    elapsed = perf_counter() - t0  # <4>
    print(f'Total time: {elapsed:.2f}s')

__ _____ __ ______
    main()
