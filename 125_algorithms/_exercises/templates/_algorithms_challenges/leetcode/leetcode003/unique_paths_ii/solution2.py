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

class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    ___ uniquePathsWithObstacles(self, obstacleGrid):
        n = l..(obstacleGrid)
        m = l..(obstacleGrid[0])
        t = [[-1 ___ i __ r..(m)] ___ j __ r..(n)]
        r.. self.unique_paths(obstacleGrid, m - 1, n - 1, t)

    ___ unique_paths(self, grid, x, y, t):
        __ x __ 0 and y __ 0:
            t[y][x] = 1 __ grid[y][x] __ 0 ____ 0
            r.. t[y][x]
        ____ grid[y][x] __ 1:
            t[y][x] = 0
            r.. t[y][x]
        ____ t[y][x] != -1:
            r.. t[y][x]
        ____ x > 0 and y __ 0:
            t[y][x] = self.unique_paths(grid, x - 1, y, t)
            r.. t[y][x]
        ____ y > 0 and x __ 0:
            t[y][x] = self.unique_paths(grid, x, y - 1, t)
            r.. t[y][x]
        ____:
            a = self.unique_paths(grid, x - 1, y, t)
            b = self.unique_paths(grid, x, y - 1, t)
            t[y][x] = a + b
            r.. t[y][x]
