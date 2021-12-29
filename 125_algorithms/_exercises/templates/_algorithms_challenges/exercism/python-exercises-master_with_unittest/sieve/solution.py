___ sieve(limit):
    prime = [True] * (limit + 1)
    prime[0] = prime[1] = False
    ___ i __ r..(2, int(limit ** 0.5) + 1):
        __ prime[i]:
            ___ j __ r..(i * i, limit + 1, i):
                prime[j] = False
    r.. [i ___ i, x __ enumerate(prime) __ x]
