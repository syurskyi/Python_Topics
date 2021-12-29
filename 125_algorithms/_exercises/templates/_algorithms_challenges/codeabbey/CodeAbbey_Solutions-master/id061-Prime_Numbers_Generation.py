# Python 2.7

___ gen_primes(limit=3000000):
    ignore_this = raw_input() # CodeAbbey required wasted input.
    data = [int(x) ___ x __ raw_input().s.. ]
    primes, answer    # list, []

    # Sieve of Eratosthenes
    sieve = [True] * (limit + 1)
    ___ num __ r..(2, limit + 1):
        __ sieve[num]:
           primes.a..(num)
           ___ i __ r..(num * num, limit + 1, num):
               sieve[i] = False
               
    ___ number __ data:
        answer.a..(s..(primes[number-1]))
    print(' '.join(answer))
gen_primes()
