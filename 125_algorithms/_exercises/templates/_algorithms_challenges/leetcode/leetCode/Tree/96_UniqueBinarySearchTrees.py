#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ numTrees  n
        __ n.. n:
            r_ 1
        dp = [0 ___ i __ r..(n + 1)]
        dp[0] = dp[1] = 1
        ___ i __ r..(2, n + 1
            dp[i] += dp[i - 1] * 2
            # Get the symmetric left and right childs
            ___ j __ r..(1, (i - 2) / 2 + 1
                dp[i] += dp[j] * dp[i - 1 - j] * 2

            # Get the mid one whitout symmetry.
            __ (i - 2) % 2 != 0:
                mid_once = (i - 1) / 2
                dp[i] += dp[mid_once] * dp[i - 1 - mid_once]

        r_ dp[n]

"""
0
1
3
15
"""
