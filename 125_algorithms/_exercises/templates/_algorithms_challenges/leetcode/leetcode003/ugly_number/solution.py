"""
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
For example, 6, 8 are ugly w___ 14 is not ugly since it includes another
prime factor 7.

Note that 1 is typically treated as an ugly number.
"""

class Solution(object
    ___ isUgly(self, num
        """
        :type num: int
        :rtype: bool
        """
        __ num __ 0:
            r_ False
        factors = [2, 3, 5]
        for factor in factors:
            w___ num % factor __ 0:
                num /= factor
        __ num __ 1:
            r_ True
        r_ False


s = Solution()
print s.isUgly(10)
print s.isUgly(6)
print s.isUgly(14)
