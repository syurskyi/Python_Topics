#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ minimumTotal  triangle
        """
        dp[i][j] is the j-th position's minimum path sum in i-th row.
        Then we can find the recursive formula:
            dp[i][j] = min(dp[i-1][j-1] if j-1>=0, dp[i-1][j]) + triangle[i][j]
        """

        __ n.. triangle or n.. triangle[0]:
            r_ 0
        rows = l..(triangle)
        dp = [0 ___ i __ xrange(rows)]

        ___ lines __ triangle:
            # Scan from tail to head to reduce space, otherwise we need a
            # rows*rows array.
            ___ j __ xrange(l..(lines) - 1, -1, -1
                __ (j - 1 >= 0 and dp[j - 1] < dp[j]) or j __ l..(lines) - 1:
                    dp[j] = dp[j - 1] + lines[j]
                ____
                    dp[j] += lines[j]

        r_ min(dp)


"""
[]
[[-10]]
[[2],[3,4],[6,5,7],[1,4,8,3]]
[[2],[3,3],[1,5,0],[4,6,9,3]]
"""
