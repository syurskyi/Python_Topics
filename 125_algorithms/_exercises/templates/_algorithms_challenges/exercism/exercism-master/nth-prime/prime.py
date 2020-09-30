______ ma__


class prime:

    @classmethod
    ___ nth_prime(cls, n
        primes =   # list
        possible = cls.possible_primes()
        w___ le.(primes) < n:
            x = next(possible)
            __ cls.is_prime(x
                primes.append(x)
        r_ primes[n - 1]

    @staticmethod
    ___ is_prime(x
        ___ i __ range(2, int(ma__.sqrt(x)) + 1
            __ x % i __ 0:
                r_ False
        r_ True

    @staticmethod
    ___ possible_primes(
        yield 2
        n = 3
        w___ True:
            yield n
            n += 2


___ nth_prime(n
    r_ prime.nth_prime(n)
