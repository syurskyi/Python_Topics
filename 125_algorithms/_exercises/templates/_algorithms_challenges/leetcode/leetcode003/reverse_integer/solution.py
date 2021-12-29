"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
"""

class Solution(object):
    ___ reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        pos = True
        __ x < 0:
            pos = False
            x = -x
        t = 0
        w.... x != 0:
            t = t * 10 + x % 10
            x /= 10
        __ n.. pos:
            r.. -t
        r.. t
