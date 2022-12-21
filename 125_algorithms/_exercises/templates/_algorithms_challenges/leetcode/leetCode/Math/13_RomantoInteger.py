#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ romanToInt  s
        """
        :type s: str
        :rtype: int
        """
        symbols_integer = {"I": 1, "V": 5, "X": 10, "L": 50,
                           "C": 100, "D": 500, "M": 1000,
                           "IV": 4, "IX": 9, "XL": 40, "XC": 90,
                           "CD": 400, "CM": 900
                           }
        length = l..(s)
        integer = 0
        isPass = False
        ___ i __ r..(length
            # Subtractive notation use this symbol
            __ isPass:
                isPass = False
                c_
            # Just add the integer
            __ s[i] __ symbols_integer a.. s[i:i + 2] n.. __ symbols_integer:
                integer = integer + symbols_integer[s[i]]
                isPass = False
                c_

            # Subtractive notation is used as follows.
            __ s[i:i + 2] __ symbols_integer:
                integer = integer + symbols_integer[s[i:i + 2]]
                isPass = True

        r_ integer

"""
"DCXXI"
"CDCM"
"""
