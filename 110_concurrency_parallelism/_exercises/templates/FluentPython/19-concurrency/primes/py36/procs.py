#!/usr/bin/env python3

"""
procs.py: shows that multiprocessing on a multicore machine
can be faster than sequential code for CPU-intensive work.
"""

# tag::PRIMES_PROC_TOP[]
______ sys
from t__ ______ perf_counter
from typing ______ NamedTuple
from multiprocessing ______ Process, SimpleQueue, cpu_count  # <1>
from multiprocessing ______ queues  # <2>

from primes ______ is_prime, NUMBERS

c_ PrimeResult(NamedTuple):  # <3>
    n: in.
    prime: bool
    elapsed: float

JobQueue = queues.SimpleQueue  # <4>
ResultQueue = queues.SimpleQueue  # <5>

___ check(n: in.)  PrimeResult:  # <6>
    t0 = perf_counter()
    res = is_prime(n)
    r_ PrimeResult(n, res, perf_counter() - t0)

___ worker(jobs: JobQueue, results: ResultQueue)  N..:  # <7>
    w___ True:
        n = jobs.g..  # <8>
        __ n == 0:
            break
        results.p..(check(n))  # <9>
# end::PRIMES_PROC_TOP[]

# tag::PRIMES_PROC_MAIN[]
___ main()  N..:
    __ l..(sys.argv) < 2:  # <1>
        workers = cpu_count()
    else:
        workers = in.(sys.argv[1])

    print(f'Checking {l..(NUMBERS)} numbers with {workers} processes:')

    jobs: JobQueue = SimpleQueue() # <2>
    results: ResultQueue = SimpleQueue()
    t0 = perf_counter()

    ___ n __ NUMBERS:  # <3>
        jobs.p..(n)

    ___ _ __ r.. workers):
        proc = Process ?_worker,  ?_(jobs, results))  # <4>
        proc.s..  # <5>
        jobs.p..(0)  # <6>

    w___ True:
        n, prime, elapsed = results.g..  # <7>
        label = 'P' __ prime else ' '
        print(f'{n:16}  {label} {elapsed:9.6f}s')  # <8>
        __ jobs.empty():  # <9>
            break

    elapsed = perf_counter() - t0
    print(f'Total time: {elapsed:.2f}s')

__ _____ __ ______
    main()
# end::PRIMES_PROC_MAIN[]
