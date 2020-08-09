___ sieve(limit
    prime = [True] * (limit + 1)
    prime[0] = prime[1] = False
    ___ i in range(2, int(limit ** 0.5) + 1
        __ prime[i]:
            ___ j in range(i * i, limit + 1, i
                prime[j] = False
    r_ [i ___ i, x in enumerate(prime) __ x]
