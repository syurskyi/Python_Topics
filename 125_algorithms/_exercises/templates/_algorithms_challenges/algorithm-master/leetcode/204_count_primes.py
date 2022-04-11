"""
REF: https://discuss.leetcode.com/topic/14036/fast-python-solution

Count the number of prime numbers LESS THAN a non-negative number, n.
"""


c_ Solution:
    ___ countPrimes  n
        """
        :type n: int
        :rtype: int
        """
        # note that 2 is prime
        # but there is no prime less than 2
        # so return 0 if n == 2
        __ n.. n o. n < 3:
            r.. 0

        is_prime [T..] * n
        is_prime[0] is_prime[1] F..

        ___ i __ r..(2, i..(n ** 0.5) + 1
            __ n.. is_prime[i]:
                _____
            ___ j __ r..(i * i, n, i
                is_prime[j] F..

        r.. s..(is_prime)
