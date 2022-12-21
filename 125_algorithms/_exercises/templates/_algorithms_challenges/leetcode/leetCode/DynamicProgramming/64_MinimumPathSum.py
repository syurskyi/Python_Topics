#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ minPathSum  grid
        __ n.. grid:
            r_ 0

        m_row = l..(grid)
        n_col = l..(grid[0])

        # dp[i][j]: the min sum along path from top left to [i,j].
        dp = [[0 ___ i __ r..(n_col)] ___ j __ r..(m_row)]

        ___ row __ r..(m_row
            ___ col __ r..(n_col
                dp[row][col] = grid[row][col]
                __ row __ 0 and col > 0:
                    dp[row][col] += dp[row][col - 1]
                ____ row > 0 and col __ 0:
                    dp[row][col] += dp[row - 1][col]
                ____ row > 0 and col > 0:
                    dp[row][col] += min(dp[row - 1][col], dp[row][col - 1])
                ____
                    pass

        r_ dp[m_row - 1][n_col - 1]


"""
[]
[[0]]
[[1,2,4,3,2,1,5],[3,4,1,2,3,5,4],[3,2,4,5,1,2,5]]
"""
