#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    MAX_INT = 2**31 - 1
    MIN_INT = - 2**31

    ___ myAtoi  strs
        """ We need to handle four cases:

        1. discards all leading whitespaces
        2. sign of the number
        3. overflow
        4. invalid input
        """
        strs = strs.strip()
        __ n.. strs:
            r_ 0

        sign, i = 1, 0
        __ strs[i] __ '+':
            i += 1
        ____ strs[i] __ '-':
            i += 1
            sign = -1

        num = 0
        _____ i < l..(strs
            __ strs[i] < '0' or strs[i] > '9':
                break
            __ num > self.MAX_INT or (num * 10 + int(strs[i]) > self.MAX_INT
                r_ self.MAX_INT __ sign __ 1 else self.MIN_INT
            ____
                num = num * 10 + int(strs[i])
            i += 1

        r_ num * sign

"""
""
"  12a"
"  a12"
"  +12"
"  +-12"
"2147483648"
"-2147483648"
"""
