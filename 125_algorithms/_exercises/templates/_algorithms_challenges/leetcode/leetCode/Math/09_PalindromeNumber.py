#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ isPalindrome  x
        __ x < 0:
            r_ F..
        reversed_x = 0
        original_x = x
        _____ x > 0:
            reversed_x = reversed_x * 10 + x % 10
            x /= 10
        r_ reversed_x __ original_x


# Pythonic way.
c.. Solution_2 o..
    ___ isPalindrome  x
        r_ x >= 0 a.. str(x) __ str(x)[::-1]


"""
9
10
-2147483648
32023
320023
98765432123456789
"""
