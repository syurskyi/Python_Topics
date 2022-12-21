#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


# Easy to understand.
c.. Solution o..
    ___ isPowerOfTwo  n
        __ n <= 0:
            r_ False
        _____ n:
            __ n & 1 and n != 1:
                r_ False
            n >>= 1
        r_ True


# Another solution: using n&(n-1) trick
c.. Solution_2 o..
    ___ isPowerOfTwo  n
        r_ n > 0 and n.. n & (n-1)

"""
-7
0
1
2
15
121
"""
