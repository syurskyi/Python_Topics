"""
Description:

Count the number of prime numbers less than a non-negative number, n.
"""
_______ math

__author__ = 'Daniel'


c_ Solution:
    ___ countPrimes  n
        """
        Find prime using Sieve's algorithm
        :type n: int
        :rtype: int
        """
        __ n < 3:
            r.. 0

        is_prime = [T.. ___ _ __ x..(n)]
        is_prime[0], is_prime[1] = F.., F..
        ___ i __ x..(2, i..(math.sqrt(n))+1
            __ is_prime[i]:
                ___ j __ x..(i*i, n, i
                    is_prime[j] = F..

        r.. is_prime.c.. T..)


__ _______ __ _______
    ... Solution().countPrimes(1500000) __ 114155