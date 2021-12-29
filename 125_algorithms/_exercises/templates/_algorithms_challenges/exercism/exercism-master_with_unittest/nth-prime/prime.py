import math


class prime:

    @classmethod
    ___ nth_prime(cls, n):
        primes = []
        possible = cls.possible_primes()
        while len(primes) < n:
            x = next(possible)
            __ cls.is_prime(x):
                primes.append(x)
        return primes[n - 1]

    @staticmethod
    ___ is_prime(x):
        for i in range(2, int(math.sqrt(x)) + 1):
            __ x % i == 0:
                return False
        return True

    @staticmethod
    ___ possible_primes():
        yield 2
        n = 3
        while True:
            yield n
            n += 2


___ nth_prime(n):
    return prime.nth_prime(n)
