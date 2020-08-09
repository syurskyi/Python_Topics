"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum
of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""
__author__ = 'Danyang'
class Solution:
    ___ minPathSum(self, grid
        """
        dp

        possible use A*
        :param grid: a list of lists of integers
        :return: integer
        """
        __ not grid:
            r_ 0

        row_cnt = le.(grid)
        col_cnt = le.(grid[0])


        dp = [[1<<31 for _ in xrange(col_cnt)] for _ in xrange(row_cnt)]

        # dp[i][j] = min(dp[i-1][j], dp[i][j-1])+grid[i][j]
        for i in xrange(row_cnt
            for j in xrange(col_cnt
                __ i__0 and j__0:
                    dp[i][j] = grid[i][j]
                ____ i__0:
                    dp[i][j] = dp[i][j-1]+grid[i][j]
                ____ j__0:
                    dp[i][j] = dp[i-1][j]+grid[i][j]
                ____
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1])+grid[i][j]  # PoP - Principle of Optimality

        r_ dp[row_cnt-1][col_cnt-1]