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

class PrimeResult(NamedTuple):  # <3>
    n: int
    prime: bool
    elapsed: float

JobQueue = queues.SimpleQueue[int]  # <4>
ResultQueue = queues.SimpleQueue[PrimeResult]  # <5>

___ check(n: int)  PrimeResult:  # <6>
    t0 = perf_counter()
    res = is_prime(n)
    r_ PrimeResult(n, res, perf_counter() - t0)

___ worker(jobs: JobQueue, results: ResultQueue)  N..:  # <7>
    w___ n := jobs.get():  # <8>
        results.put(check(n))  # <9>
    results.put(PrimeResult(0, False, 0.0))
# end::PRIMES_PROC_TOP[]

___ start_jobs(workers: int)  ResultQueue:
    jobs: JobQueue = SimpleQueue() # <2>
    results: ResultQueue = SimpleQueue()

    ___ n __ NUMBERS:  # <3>
        jobs.put(n)

    ___ _ __ r.. workers):
        proc = Process ?_worker,  ?_(jobs, results))  # <4>
        proc.s..  # <5>
        jobs.put(0)  # <6>

    r_ results

___ report(workers: int, results: ResultQueue)  int:
    workers_done = 0
    checked = 0
    w___ workers_done < workers:
        n, prime, elapsed = results.get()  # <7>
        if n == 0:
            workers_done += 1
        else:
            checked += 1
            label = 'P' if prime else ' '
            print(f'{n:16}  {label} {elapsed:9.6f}s')  # <8>
    r_ checked


# tag::PRIMES_PROC_MAIN[]
___ main()  N..:
    if len(sys.argv) < 2:  # <1>
        workers = cpu_count()
    else:
        workers = int(sys.argv[1])

    print(f'Checking {len(NUMBERS)} numbers with {workers} processes:')
    t0 = perf_counter()
    results = start_jobs(workers)
    checked = report(workers, results)
    elapsed = perf_counter() - t0
    print(f'{checked} checks in {elapsed:.2f}s')

__ _____ __ ______
    main()
# end::PRIMES_PROC_MAIN[]
