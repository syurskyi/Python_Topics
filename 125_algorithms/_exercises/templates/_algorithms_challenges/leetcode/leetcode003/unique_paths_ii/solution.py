"""
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths
would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.
"""

c_ Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    ___ uniquePathsWithObstacles(self, obstacleGrid):
        grid = obstacleGrid
        n = l..(grid)
        m = l..(grid[0])
        t = [[-1 ___ i __ r..(m)] ___ j __ r..(n)]
        ___ i __ r..(n):
            ___ j __ r..(m):
                __ grid[i][j] __ 1:
                    t[i][j] = 0
                ____:
                    __ i __ 0 a.. j __ 0:
                        t[i][j] = 1
                    ____ i __ 0:
                        t[i][j] = t[i][j - 1]
                    ____ j __ 0:
                        t[i][j] = t[i - 1][j]
                    ____:
                        t[i][j] = t[i - 1][j] + t[i][j - 1]
        r.. t[n - 1][m - 1]
