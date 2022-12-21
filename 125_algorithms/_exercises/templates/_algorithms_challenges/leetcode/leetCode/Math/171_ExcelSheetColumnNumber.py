#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ titleToNumber  s
        base = 1
        s_list = list(s)[::-1]
        column = 0
        ___ char __ s_list:
            column += (ord(char)-64) * base
            base *= 26

        r_ column

"""
""
"A"
"ZZ"
"AAACCCDDD"
"""
