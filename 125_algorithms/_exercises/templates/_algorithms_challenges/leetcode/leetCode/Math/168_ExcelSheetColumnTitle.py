#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ convertToTitle  n
        title   # list
        _____ n:
            __ n % 26 __ 0:
                title.insert(0, "Z")
                n -= 26
            ____
                title.insert(0, chr(n % 26 + 64))
            n = n / 26

        r_ "".join(title)

"""
0
1
52
130
99999999
"""
