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

c_ PrimeResult(NamedTuple):
    n: in.
    prime: bool
    elapsed: float

JobQueue = SimpleQueue[in.]  # <4>
ResultQueue = SimpleQueue[PrimeResult]  # <5>

___ check(n: in.)  PrimeResult:  # <6>
    t0 = perf_counter()
    res = is_prime(n)
    r_ PrimeResult(n, res, perf_counter() - t0)

___ worker(jobs: JobQueue, results: ResultQueue)  N..:  # <7>
    w___ n := jobs.g..:  # <8>
        results.p..(check(n))  # <9>
    results.p..(PrimeResult(0, F.., 0.0))

___ start_jobs(workers: in., jobs: JobQueue, results: ResultQueue)  N..:
    ___ n __ NUMBERS:  # <3>
        jobs.p..(n)
    ___ _ __ r.. workers):
        proc = ? ?_worker,  ?_(jobs, results))  # <4>
        proc.s..  # <5>
        jobs.p..(0)  # <6>

___ report(workers: in., results: ResultQueue)  in.:
    checked = 0
    workers_done = 0
    w___ workers_done < workers:
        n, prime, elapsed = results.g..
        __ n == 0:
            workers_done += 1
        else:
            checked += 1
            label = 'P' __ prime else ' '
            print(f'{n:16}  {label} {elapsed:9.6f}s')
    r_ checked

___ main()  N..:
    __ l..(sys.argv) < 2:
        workers = os.cpu_count()
    else:
        workers = in.(sys.argv[1])

    print(f'Checking {l..(NUMBERS)} numbers with {workers} threads:')
    t0 = perf_counter()
    jobs: JobQueue = SimpleQueue()
    results: ResultQueue = SimpleQueue()
    start_jobs(workers, jobs, results)
    checked = report(workers, results)
    elapsed = perf_counter() - t0
    print(f'{checked} checks in {elapsed:.2f}s')

__ _____ __ ______
    main()

