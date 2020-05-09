#/usr/bin/env python3


___ sieve_of_eratosthenes(n
    """
    Gets you all the primes from 1 to n
    """

    A _ [True] * n
    A[0] _ False
    A[1] _ False

    for i, isprime in enumerate(A

        if isprime:
            yield i

            for x in range(i * i, n, i
                A[x] _ False
