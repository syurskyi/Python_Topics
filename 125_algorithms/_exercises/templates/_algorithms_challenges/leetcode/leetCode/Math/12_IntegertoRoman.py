#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ intToRoman  num
        """
        :type num: int
        :rtype: str
        """
        integer_symbols = [["I", "IV", "V", "IX"],
                           ["X", "XL", "L", "XC"],
                           ["C", "CD", "D", "CM"],
                           ["M"]
                           ]
        roman_str = ""
        counter = 0

        _____ num != 0:
            single = num % 10

            __ single __ [1, 2, 3]:
                roman_str = single * integer_symbols[counter][0] + roman_str
            ____ single __ 4:
                roman_str = integer_symbols[counter][1] + roman_str
            ____ single __ 5:
                roman_str = integer_symbols[counter][2] + roman_str
            ____ single __ [6, 7, 8]:
                roman_str = integer_symbols[counter][2] +\
                    (single - 5) * integer_symbols[counter][0] +\
                    roman_str
            ____ single __ 9:
                roman_str = integer_symbols[counter][3] + roman_str
            ____
                num = num / 10
                counter += 1
                c_
            num = num / 10
            counter += 1

        r_ roman_str

"""
1
100
3999
"""
