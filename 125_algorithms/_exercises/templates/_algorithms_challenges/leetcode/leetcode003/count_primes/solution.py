"""
Description:

Count the number of prime numbers less than a non-negative number, n.

Hint:

Let's start with a isPrime function. To determine if a number is prime, we
need to check if it is not divisible by any number less than n. The runtime
complexity of isPrime function would be O(n) and hence counting the total
prime numbers up to n would be O(n2). Could we do better?

"""

c_ Solution(o..
    ___ countPrimes  n
        """
        :type n: int
        :rtype: int
        """
        res = 0
        ___ i __ r..(2, n
            __ is_prime(i
                res += 1
        r.. res

    ___ is_prime  k
        i = 2
        w.... i * i <= k:
            __ k % i __ 0:
                r.. F..
            i += 1
        r.. T..


s = Solution()
print(s.countPrimes(500))
