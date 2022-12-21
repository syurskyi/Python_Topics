#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ climbStairs  n
        """
        :type n: int
        :rtype: int
        """
        __ n.. n:
            r_ 1

        dp = [0 ___ i __ r..(n)]
        dp[0] = 1
        __ n > 1:
            dp[1] = 2
        ___ i __ r..(2, n
            dp[i] = dp[i-1] + dp[i-2]

        r_ dp[n-1]
