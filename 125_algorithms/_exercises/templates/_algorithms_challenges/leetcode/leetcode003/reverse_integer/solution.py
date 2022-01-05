"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
"""

c_ Solution(object):
    ___ reverse  x):
        """
        :type x: int
        :rtype: int
        """
        pos = T..
        __ x < 0:
            pos = F..
            x = -x
        t = 0
        w.... x != 0:
            t = t * 10 + x % 10
            x /= 10
        __ n.. pos:
            r.. -t
        r.. t
