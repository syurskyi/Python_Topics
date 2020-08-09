"""Finds primes numbers"""

___ sieve(lim
    """Implimentation of sieve of Eratosthenes"""
    multiples = set()
    primes = [2,]
    for num in range(3, lim+1, 2
        __ num not in multiples:
            primes.append(num)
            multiples.update(range(num**2, lim, num))
    r_ primes
