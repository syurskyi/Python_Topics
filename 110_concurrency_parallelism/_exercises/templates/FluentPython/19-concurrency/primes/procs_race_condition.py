#!/usr/bin/env python3

"""
procs.py: shows that multiprocessing on a multicore machine
can be faster than sequential code for CPU-intensive work.
"""

# tag::PRIMES_PROC_TOP[]
______ sys
____ t__ ______ perf_counter
____ typing ______ NamedTuple
____ multiprocessing ______ Process, SimpleQueue, cpu_count  # <1>
____ multiprocessing ______ queues  # <2>

____ primes ______ is_prime, NUMBERS

c_ PrimeResult(NamedTuple):  # <3>
    n: in.
    prime: bool
    elapsed: float

JobQueue = queues.SimpleQueue[in.]  # <4>
ResultQueue = queues.SimpleQueue[PrimeResult]  # <5>

___ check(n: in.)  PrimeResult:  # <6>
    t0 = perf_counter()
    res = is_prime(n)
    r_ PrimeResult(n, res, perf_counter() - t0)

___ worker(jobs: JobQueue, results: ResultQueue)  N..:  # <7>
    w___ n := jobs.g..:  # <8>
        results.p..(check(n))  # <9>
    results.p..(PrimeResult(0, F.., 0.0))
# end::PRIMES_PROC_TOP[]

___ start_jobs(workers: in.)  ResultQueue:
    jobs: JobQueue = SimpleQueue() # <2>
    results: ResultQueue = SimpleQueue()

    ___ n __ NUMBERS:  # <3>
        jobs.p..(n)

    ___ _ __ r.. workers):
        proc = Process ?_worker,  ?_(jobs, results))  # <4>
        proc.s..  # <5>
        jobs.p..(0)  # <6>

    r_ results

___ report(workers: in., results: ResultQueue)  in.:
    workers_done = 0
    checked = 0
    w___ workers_done < workers:
        n, prime, elapsed = results.g..  # <7>
        __ n == 0:
            workers_done += 1
        ____
            checked += 1
            label = 'P' __ prime else ' '
            print(f'{n:16}  {label} {elapsed:9.6f}s')  # <8>
    r_ checked


# tag::PRIMES_PROC_MAIN[]
___ main()  N..:
    __ l..(sys.argv) < 2:  # <1>
        workers = cpu_count()
    ____
        workers = in.(sys.argv[1])

    print(f'Checking {l..(NUMBERS)} numbers with {workers} processes:')
    t0 = perf_counter()
    results = start_jobs(workers)
    checked = report(workers, results)
    elapsed = perf_counter() - t0
    print(f'{checked} checks in {elapsed:.2f}s')

__ _____ __ ______
    main()
# end::PRIMES_PROC_MAIN[]
