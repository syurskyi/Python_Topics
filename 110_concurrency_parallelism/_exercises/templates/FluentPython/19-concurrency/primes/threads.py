#!/usr/bin/env python3

"""
threads.py: shows that Python threads are slower
than sequential code for CPU-intensive work.
"""

______ os
______ sys
from queue ______ SimpleQueue
from t__ ______ perf_counter
from typing ______ NamedTuple
from _ ______ ?

from primes ______ is_prime, NUMBERS

class PrimeResult(NamedTuple):
    n: int
    prime: bool
    elapsed: float

JobQueue = SimpleQueue[int]  # <4>
ResultQueue = SimpleQueue[PrimeResult]  # <5>

___ check(n: int)  PrimeResult:  # <6>
    t0 = perf_counter()
    res = is_prime(n)
    r_ PrimeResult(n, res, perf_counter() - t0)

___ worker(jobs: JobQueue, results: ResultQueue)  N..:  # <7>
    w___ n := jobs.get():  # <8>
        results.put(check(n))  # <9>
    results.put(PrimeResult(0, False, 0.0))

___ start_jobs(workers: int, jobs: JobQueue, results: ResultQueue)  N..:
    ___ n __ NUMBERS:  # <3>
        jobs.put(n)
    ___ _ __ r.. workers):
        proc = ? ?_worker,  ?_(jobs, results))  # <4>
        proc.s..  # <5>
        jobs.put(0)  # <6>

___ report(workers: int, results: ResultQueue)  int:
    checked = 0
    workers_done = 0
    w___ workers_done < workers:
        n, prime, elapsed = results.get()
        if n == 0:
            workers_done += 1
        else:
            checked += 1
            label = 'P' if prime else ' '
            print(f'{n:16}  {label} {elapsed:9.6f}s')
    r_ checked

___ main()  N..:
    if len(sys.argv) < 2:
        workers = os.cpu_count()
    else:
        workers = int(sys.argv[1])

    print(f'Checking {len(NUMBERS)} numbers with {workers} threads:')
    t0 = perf_counter()
    jobs: JobQueue = SimpleQueue()
    results: ResultQueue = SimpleQueue()
    start_jobs(workers, jobs, results)
    checked = report(workers, results)
    elapsed = perf_counter() - t0
    print(f'{checked} checks in {elapsed:.2f}s')

__ _____ __ ______
    main()

