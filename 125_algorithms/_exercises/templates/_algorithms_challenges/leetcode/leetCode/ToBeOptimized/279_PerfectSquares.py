#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


# Dynamic Programming with static variable
c.. Solution o..
    # Since dp is a static vector, we have already calculated the result
    # during previous function calls and we can just return the result now.
    _dp = [0]

    ___ numSquares  n
        dp = self._dp
        _____ l..(dp) <= n:
            i = l..(dp)
            min_count = 2 ** 31 - 1
            ___ j __ r..(1, int(i**0.5) + 1
                min_count = m.. min_count, dp[i-j*j]+1)
            dp.a.. min_count)
        r_ dp[n]


# Dynamic Programming
# Easy to undersrtand but unfortually "Time Limit Exceeded"
c.. Solution_2 o..
    ___ numSquares  n
        dp = [0] * (n+1)
        ___ i __ r..(1, n+1
            min_count = 2 ** 31 - 1
            ___ j __ r..(1, int(i**0.5) + 1
                min_count = m.. min_count, dp[i-j*j]+1)
            dp[i] = min_count
        r_ dp[n]

"""
1
12
13
156
"""
