#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# @Last Modified time: 2016-07-04 11:44:22


c.. Solution o..
    # Binary Search
    ___ isPerfectSquare  num
        low, high = 0, num
        _____ low <= high:
            mid = (low + high) / 2
            __ mid ** 2 __ num:
                r_ True
            ____ mid ** 2 > num:
                high = mid - 1
            ____
                low = mid + 1
        r_ False


c.. Solution_2 o..
    # Truth: A square number is 1+3+5+7+...  Time Complexity O(sqrt(N))
    ___ isPerfectSquare  num
        i = 1
        _____ num > 0:
            num -= i
            i += 2
        r_ num __ 0


c.. Solution_3 o..
    # Newton Method.  Time Complexity is close to constant.
    # According to: https://en.wikipedia.org/wiki/Newton%27s_method
    ___ isPerfectSquare  num
        val = num
        _____ val ** 2 > num:
            val = (val + num / val) / 2
        r_ val * val __ num

"""
0
1
121
12321
2147483647
"""
