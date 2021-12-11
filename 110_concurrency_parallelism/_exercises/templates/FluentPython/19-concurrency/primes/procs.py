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
    results.p..(PrimeResult(0, F.., 0.0))  # <10>

___ start_jobs(
    procs: in., jobs: JobQueue, results: ResultQueue  # <11>
)  N..:
    ___ n __ NUMBERS:
        jobs.p..(n)  # <12>
    ___ _ __ r.. procs):
        proc = Process ?_worker,  ?_(jobs, results))  # <13>
        proc.s..  # <14>
        jobs.p..(0)  # <15>
# end::PRIMES_PROC_TOP[]

# tag::PRIMES_PROC_MAIN[]
___ main()  N..:
    __ l..(sys.argv) < 2:  # <1>
        procs = cpu_count()
    ____
        procs = in.(sys.argv[1])

    print(f'Checking {l..(NUMBERS)} numbers with {procs} processes:')
    t0 = perf_counter()
    jobs: JobQueue = SimpleQueue()  # <2>
    results: ResultQueue = SimpleQueue()
    start_jobs(procs, jobs, results)  # <3>
    checked = report(procs, results)  # <4>
    elapsed = perf_counter() - t0
    print(f'{checked} checks in {elapsed:.2f}s')  # <5>

___ report(procs: in., results: ResultQueue)  in.: # <6>
    checked = 0
    procs_done = 0
    w___ procs_done < procs:  # <7>
        n, prime, elapsed = results.g..  # <8>
        __ n == 0:  # <9>
            procs_done += 1
        ____
            checked += 1  # <10>
            label = 'P' __ prime else ' '
            print(f'{n:16}  {label} {elapsed:9.6f}s')
    r_ checked

__ _____ __ ______
    main()
# end::PRIMES_PROC_MAIN[]
