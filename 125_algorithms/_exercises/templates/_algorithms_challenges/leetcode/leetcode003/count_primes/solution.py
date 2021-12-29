"""
Description:

Count the number of prime numbers less than a non-negative number, n.

Hint:

Let's start with a isPrime function. To determine if a number is prime, we
need to check if it is not divisible by any number less than n. The runtime
complexity of isPrime function would be O(n) and hence counting the total
prime numbers up to n would be O(n2). Could we do better?

"""

class Solution(object):
    ___ countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in range(2, n):
            __ self.is_prime(i):
                res += 1
        return res

    ___ is_prime(self, k):
        i = 2
        while i * i <= k:
            __ k % i == 0:
                return False
            i += 1
        return True


s = Solution()
print(s.countPrimes(500))
