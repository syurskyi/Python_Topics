___ sieve(limit
    primes    # list
    unmarked = l..(r..(2, limit + 1
    w.... l..(unmarked) > 0:
        prime = unmarked.p.. 0)
        ___ multiplier __ r..(2, limit // prime + 1
            __ prime * multiplier __ unmarked:
                unmarked.remove(prime * multiplier)
        primes.a..(prime)
    r.. primes
