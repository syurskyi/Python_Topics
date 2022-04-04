"""
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
"""

c_ Solution(o..
    ___ trailingZeroes  n
        """
        :type n: int
        :rtype: int
        """
        res = 0
        i = 5
        w.... n / i >_ 1:
            res += n / i
            i *= 5
        r.. res
