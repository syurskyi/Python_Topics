#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    # Binary search.
    ___ mySqrt  x
        low, high = 0, x
        _____ low <= high:
            mid = (low + high) / 2
            __ mid ** 2 <= x < (mid + 1) ** 2:
                r_ mid
            ____ mid ** 2 > x:
                high = mid - 1
            ____
                low = mid + 1


c.. Solution_2 o..
    # Newton iterative method
    # According to:
    # http://www.matrix67.com/blog/archives/361
    ___ mySqrt  x
        __ n.. x:
            r_ x
        val = x
        sqrt_x = (val + x * 1.0 / val) / 2.0
        _____ val - sqrt_x > 0.001:
            val = sqrt_x
            sqrt_x = (val + x * 1.0 / val) / 2.0

        r_ int(sqrt_x)


c.. Solution_3 o..
    # Shorter Newton method.
    ___ mySqrt  x
        val = x
        _____ val * val > x:
            val = (val + x / val) / 2
        r_ val

"""
0
1
15
90
1010
"""
