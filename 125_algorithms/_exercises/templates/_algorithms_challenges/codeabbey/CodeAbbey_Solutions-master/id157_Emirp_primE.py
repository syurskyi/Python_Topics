# Python 3.4
# Note -- The solution is currently a work-in-progress
# It works, but takes a brute-force method that will only
# work on realistic numbers (ie: not a quintillion)

___ find_answer(entry):
    ___ emirp __ semirp:
        __ emirp > entry:
            r.. emirp

___ gen_primes(limit=300000000):
    data = [int(input()) ___ x __ r..(int(input()))]
    primes, semirp, answer    # list, [], []
    global semirp

    # Sieve of Eratosthenes
    sieve = [True] * (limit + 1)
    ___ num __ r..(2, limit + 1):
        __ sieve[num]:
           primes.a..(num)
           ___ i __ r..(num * num, limit + 1, num):
               sieve[i] = False

    # Find reversable primes
    ___ prime __ primes:
        __ int(str(prime)[::-1]) __ primes:
            semirp.a..(prime)

    # Find answer
    ___ entry __ data:
        answer.a..(str(find_answer(entry)))

    print(' '.join(answer))
gen_primes()
