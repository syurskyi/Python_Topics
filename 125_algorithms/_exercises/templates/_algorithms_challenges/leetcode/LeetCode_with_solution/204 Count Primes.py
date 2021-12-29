"""
Description:

Count the number of prime numbers less than a non-negative number, n.
"""
_______ math

__author__ = 'Daniel'


class Solution:
    ___ countPrimes(self, n):
        """
        Find prime using Sieve's algorithm
        :type n: int
        :rtype: int
        """
        __ n < 3:
            r.. 0

        is_prime = [True ___ _ __ xrange(n)]
        is_prime[0], is_prime[1] = False, False
        ___ i __ xrange(2, int(math.sqrt(n))+1):
            __ is_prime[i]:
                ___ j __ xrange(i*i, n, i):
                    is_prime[j] = False

        r.. is_prime.c.. True)


__ __name__ __ "__main__":
    ... Solution().countPrimes(1500000) __ 114155