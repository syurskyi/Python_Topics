#/usr/bin/env python3


def sieve_of_eratosthenes(n):
    """
    Gets you all the primes from 1 to n
    """

    A = [True] * n
    A[0] = False
    A[1] = False

    for i, isprime in enumerate(A):

        if isprime:
            yield i

            for x in range(i * i, n, i):
                A[x] = False
