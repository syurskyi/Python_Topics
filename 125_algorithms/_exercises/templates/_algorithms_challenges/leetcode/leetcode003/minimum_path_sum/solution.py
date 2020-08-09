"""
Given a m x n grid filled with non-negative numbers, find a path from top left
to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""

class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    ___ minPathSum(self, grid
        n = le.(grid)
        m = le.(grid[0])
        t = [[0 for i in range(m)] for j in range(n)]
        for i in range(n
            for j in range(m
                __ i __ 0 and j __ 0:
                    t[i][j] = grid[i][j]
                ____ i __ 0:
                    t[i][j] = grid[i][j] + t[i][j - 1]
                ____ j __ 0:
                    t[i][j] = grid[i][j] + t[i - 1][j]
                ____
                    t[i][j] = grid[i][j] + min(t[i - 1][j], t[i][j - 1])
        r_ t[n - 1][m - 1]
