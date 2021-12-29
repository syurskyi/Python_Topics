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
        t = [[-1 ___ i __ r..(m)] ___ j __ r..(n)]
        r.. self.min_path_sum_aux(grid, m - 1, n - 1, t)

    ___ min_path_sum_aux(self, grid, x, y, t):
        __ x __ 0 a.. y __ 0:
            r.. grid[y][x]
        ____ t[y][x] != -1:
            r.. t[y][x]
        ____ x __ 0 a.. y > 0:
            t[y][x] = grid[y][x] + self.min_path_sum_aux(grid, x, y - 1, t)
            r.. t[y][x]
        ____ x > 0 a.. y __ 0:
            t[y][x] = grid[y][x] + self.min_path_sum_aux(grid, x - 1, y, t)
            r.. t[y][x]
        ____:
            a = self.min_path_sum_aux(grid, x - 1, y, t)
            b = self.min_path_sum_aux(grid, x, y - 1, t)
            t[y][x] = grid[y][x] + m..(a, b)
            r.. t[y][x]
