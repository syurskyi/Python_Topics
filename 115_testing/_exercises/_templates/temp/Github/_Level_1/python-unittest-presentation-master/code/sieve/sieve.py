#/usr/bin/env python3


___ sieve_of_eratosthenes(n
    """
    Gets you all the primes from 1 to n
    """

    A _ [T..] * n
    A[0] _ F..
    A[1] _ F..

    for i, isprime in enumerate(A

        __ isprime:
            yield i

            for x in range(i * i, n, i
                A[x] _ F..
