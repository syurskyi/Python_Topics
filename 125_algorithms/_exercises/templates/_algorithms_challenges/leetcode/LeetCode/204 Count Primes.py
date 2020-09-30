"""
Description:

Count the number of prime numbers less than a non-negative number, n.
"""
______ ma__

__author__ = 'Daniel'


class Solution:
    ___ countPrimes(self, n
        """
        Find prime using Sieve's algorithm
        :type n: int
        :rtype: int
        """
        __ n < 3:
            r_ 0

        is_prime = [True ___ _ __ xrange(n)]
        is_prime[0], is_prime[1] = False, False
        ___ i __ xrange(2, int(ma__.sqrt(n))+1
            __ is_prime[i]:
                ___ j __ xrange(i*i, n, i
                    is_prime[j] = False

        r_ is_prime.count(True)


__  -n __ "__main__":
    assert Solution().countPrimes(1500000) __ 114155