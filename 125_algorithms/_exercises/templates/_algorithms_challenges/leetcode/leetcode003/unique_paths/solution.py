"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in
the diagram below).

The robot can only move either down or right at any point in time. The robot
is trying to reach the bottom-right corner of the grid (marked 'Finish' in the
diagram below).

How many possible unique paths are there?
"""

c_ Solution:
    # @return an integer
    ___ uniquePaths(self, m, n):
        t = [[1] * m] * n
        i = j = 0
        ___ i __ r..(n):
            ___ j __ r..(m):
                __ i __ 0 a.. j __ 0:
                    continue
                ____ i __ 0:
                    t[i][j] = 1
                ____ j __ 0:
                    t[i][j] = 1
                ____:
                    t[i][j] = t[i - 1][j] + t[i][j - 1]
        r.. t[n - 1][m - 1]
