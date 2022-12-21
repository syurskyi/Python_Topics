#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# @Last Modified time: 2016-06-26 20:08:14


c.. Solution o..
    ___ myPow  x, n
        abs_half = abs(n) / 2

        __ n __ 0:
            r_ 1.00

        ____ n > 0:
            result = self.myPow(x * x, abs_half)
            __ n & 1 __ 1:
                result *= x
            r_ result

        ____
            result = 1 / self.myPow(x * x, abs_half)
            __ abs(n) & 1 __ 1:
                result *= 1 / x
            r_ result

"""
8.88023
3
2
1
2.2
-100
"""
