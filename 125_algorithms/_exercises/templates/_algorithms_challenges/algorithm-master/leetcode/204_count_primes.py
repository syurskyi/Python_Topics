"""
REF: https://discuss.leetcode.com/topic/14036/fast-python-solution

Count the number of prime numbers LESS THAN a non-negative number, n.
"""


class Solution:
    ___ countPrimes(self, n
        """
        :type n: int
        :rtype: int
        """
        # note that 2 is prime
        # but there is no prime less than 2
        # so return 0 if n == 2
        __ not n or n < 3:
            r_ 0

        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False

        ___ i in range(2, int(n ** 0.5) + 1
            __ not is_prime[i]:
                continue
            ___ j in range(i * i, n, i
                is_prime[j] = False

        r_ su.(is_prime)
