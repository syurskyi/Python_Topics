___ sieve(limit
    primes = []
    unmarked = list(range(2, limit + 1))
    w___ le.(unmarked) > 0:
        prime = unmarked.pop(0)
        ___ multiplier in range(2, limit // prime + 1
            __ prime * multiplier in unmarked:
                unmarked.remove(prime * multiplier)
        primes.append(prime)
    r_ primes
