"""
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
For example, 6, 8 are ugly while 14 is not ugly since it includes another
prime factor 7.

Note that 1 is typically treated as an ugly number.
"""

class Solution(object):
    ___ isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        __ num == 0:
            return False
        factors = [2, 3, 5]
        for factor in factors:
            while num % factor == 0:
                num /= factor
        __ num == 1:
            return True
        return False


s = Solution()
print s.isUgly(10)
print s.isUgly(6)
print s.isUgly(14)
