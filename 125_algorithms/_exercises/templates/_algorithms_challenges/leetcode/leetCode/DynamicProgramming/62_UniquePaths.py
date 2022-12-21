#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ uniquePaths  m, n
        # Dynamic Programming.
        # dp[i][j]: present unique paths from (0, 0) to (i-1, j-1)
        dp = [[1 ___ i __ r..(n)] ___ j __ r..(m)]
        ___ row __ r..(1, m
            ___ col __ r..(1, n
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

        r_ dp[m - 1][n - 1]


c.. Solution_2 o..
    ___ uniquePaths  m, n
        """ Using formula.

        Choose (n - 1) movements(number of steps to the right) from (m + n - 2),
        and rest (m - 1) is (number of steps down).
        We calculate the total possible path number
        Combination(N, k) = n! / (k!(n - k)!)
        reduce the numerator and denominator and get
        C = ( (n - k + 1) * (n - k + 2) * ... * n ) / k!
        """
        N, K = m + n - 2, min(n, m) - 1
        path_cnts = 1
        ___ i __ xrange(1, K + 1
            path_cnts = path_cnts * (N - K + i) / i

        r_ path_cnts

"""
0
5
3
8
87
99
"""
