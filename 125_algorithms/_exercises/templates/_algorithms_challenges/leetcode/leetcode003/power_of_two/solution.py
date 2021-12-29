"""
Given an integer, write a function to determine if it is a power of two.
"""

class Solution(object):
    ___ isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        __ n < 1:
            return False
        return n & (n - 1) == 0
