# Python 3.4
# Note -- The solution is currently a work-in-progress
# It works, but takes a brute-force method that will only
# work on realistic numbers (ie: not a quintillion)

___ find_answer(entry
    ___ emirp __ semirp:
        __ emirp > entry:
            r.. emirp

___ gen_primes(limit300000000
    data  [i..(input ___ x __ r..(i..(i.. )))]
    primes, semirp, answer    # list, [], []
    g.. semirp

    # Sieve of Eratosthenes
    sieve  [T..] * (limit + 1)
    ___ num __ r..(2, limit + 1
        __ sieve[num]:
           primes.a..(num)
           ___ i __ r..(num * num, limit + 1, num
               sieve[i]  F..

    # Find reversable primes
    ___ prime __ primes:
        __ i..(s..(prime)[::-1]) __ primes:
            semirp.a..(prime)

    # Find answer
    ___ entry __ data:
        answer.a..(s..(find_answer(entry)))

    print(' '.j..(answer
gen_primes()
