"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum
of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""
__author__ = 'Danyang'
c_ Solution:
    ___ minPathSum  grid):
        """
        dp

        possible use A*
        :param grid: a list of lists of integers
        :return: integer
        """
        __ n.. grid:
            r.. 0

        row_cnt = l..(grid)
        col_cnt = l..(grid[0])


        dp = [[1<<31 ___ _ __ xrange(col_cnt)] ___ _ __ xrange(row_cnt)]

        # dp[i][j] = min(dp[i-1][j], dp[i][j-1])+grid[i][j]
        ___ i __ xrange(row_cnt):
            ___ j __ xrange(col_cnt):
                __ i__0 a.. j__0:
                    dp[i][j] = grid[i][j]
                ____ i__0:
                    dp[i][j] = dp[i][j-1]+grid[i][j]
                ____ j__0:
                    dp[i][j] = dp[i-1][j]+grid[i][j]
                ____:
                    dp[i][j] = m..(dp[i-1][j], dp[i][j-1])+grid[i][j]  # PoP - Principle of Optimality

        r.. dp[row_cnt-1][col_cnt-1]