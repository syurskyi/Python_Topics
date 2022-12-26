#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


c.. Solution o..
    # Just get the conclusion from the following second way.
    ___ canWinNim  n
        __ n % 4:
            r_ True
        ____
            r_ F..


c.. Solution_2 o..
    # Easy to understand, need more memory.
    # Can be optimized by using static variable.
    ___ canWinNim  n
        dp = [True] * (n+1)
        __ n > 3:
            dp[4] = F..
            ___ i __ r..(5, n+1
                __ dp[i-1] a.. dp[i-2] a.. dp[i-3]:
                    dp[i] = F..
        r_ dp[n]

"""
1
8
12
245
12345
"""
