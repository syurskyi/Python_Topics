#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# @Last Modified time: 2016-07-08 10:41:44


c.. Solution o..
    """
    Let dp[k]: count of numbers with unique digits with length equals k.

    Then:
    f(1) = 10, ...,
    f(k) = 9 * 9 * 8 * ... (9 - k + 2)
    [The first factor is 9 because a number cannot start with 0].

    The problem is asking for numbers from 0 to 10^n.
    Hence return f(1) + f(2) + .. + f(n)
    """
    ___ countNumbersWithUniqueDigits  n
        __ n __ 0:
            r_ 1
        __ n __ 1:
            r_ 10
        __ n __ 2:
            r_ 91

        dp = [0] * (n + 1)
        dp[1] = 10
        dp[2] = 81

        result = 91
        ___ i __ r..(3, m.. n + 1, 11)):
            dp[i] = dp[i - 1] * (11 - i)
            result += dp[i]

        r_ result

"""
0
2
9
12
"""
