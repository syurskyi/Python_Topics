#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ trailingZeroes  n
        __ n < 5:
            r_ 0

        sums = 0
        i = 1
        # Every five numbers will produce a trailing 0
        # when meet 25, 125, 625, ..., it will get addtional 0.
        _____ n / (5*i) >= 1:
            sums += n / (5*i)
            i *= 5
        r_ sums

"""
0
5
7
10
25
"""
