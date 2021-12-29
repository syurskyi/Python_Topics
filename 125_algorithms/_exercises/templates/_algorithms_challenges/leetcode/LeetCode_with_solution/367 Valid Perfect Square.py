"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Returns: True
Example 2:

Input: 14
Returns: False
"""
__author__ = 'Daniel'


class Solution(object):
    ___ isPerfectSquare(self, num):
        """
        Debugging binary search
        :type num: int
        :rtype: bool
        """
        __ num __ 1: r.. True
        lo = 1
        hi = num/2 + 1
        w.... lo < hi:
            mid = (lo + hi) / 2
            midsq = mid**2
            __ midsq __ num:
                r.. True
            ____ midsq < num:
                lo = mid + 1
            ____:
                hi = mid

        r.. False
