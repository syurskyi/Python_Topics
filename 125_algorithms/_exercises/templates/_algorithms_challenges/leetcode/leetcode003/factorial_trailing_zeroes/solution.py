"""
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
"""

c_ Solution(object):
    ___ trailingZeroes  n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        i = 5
        w.... n / i >= 1:
            res += n / i
            i *= 5
        r.. res
