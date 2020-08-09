# Python 2.7

___ gen_primes(limit=3000000
    ignore_this = raw_input() # CodeAbbey required wasted input.
    data = [int(x) ___ x in raw_input().split()]
    primes, answer = [], []

    # Sieve of Eratosthenes
    sieve = [True] * (limit + 1)
    ___ num in range(2, limit + 1
        __ sieve[num]:
           primes.append(num)
           ___ i in range(num * num, limit + 1, num
               sieve[i] = False
               
    ___ number in data:
        answer.append(str(primes[number-1]))
    print(' '.join(answer))
gen_primes()
