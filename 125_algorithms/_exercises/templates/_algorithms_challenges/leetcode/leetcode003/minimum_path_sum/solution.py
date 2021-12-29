"""
Given a m x n grid filled with non-negative numbers, find a path from top left
to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""

class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    ___ minPathSum(self, grid):
        n = l..(grid)
        m = l..(grid[0])
        t = [[0 ___ i __ r..(m)] ___ j __ r..(n)]
        ___ i __ r..(n):
            ___ j __ r..(m):
                __ i __ 0 a.. j __ 0:
                    t[i][j] = grid[i][j]
                ____ i __ 0:
                    t[i][j] = grid[i][j] + t[i][j - 1]
                ____ j __ 0:
                    t[i][j] = grid[i][j] + t[i - 1][j]
                ____:
                    t[i][j] = grid[i][j] + m..(t[i - 1][j], t[i][j - 1])
        r.. t[n - 1][m - 1]
