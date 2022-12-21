#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ uniquePathsWithObstacles  obstacleGrid
        m = l..(obstacleGrid)
        __ n.. m:
            r_ 0
        n = l..(obstacleGrid[0])

        # dp[i][j] unique paths from (0, 0) to (i-1, j-1)
        dp = [[0 ___ i __ r..(n + 1)] ___ j __ r..(m + 1)]
        dp[0][1] = 1
        ___ i __ xrange(1, m + 1
            ___ j __ xrange(1, n + 1
                # If there is a obstacle at (i,j), then dp[i][j] = 0
                __ n.. obstacleGrid[i - 1][j - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        r_ dp[m][n]


"""
[[0]]
[[0,0,0],[0,1,0],[0,0,0]]
[[0,0,0,0],[0,0,1,1],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
[[1],[0]]
"""
