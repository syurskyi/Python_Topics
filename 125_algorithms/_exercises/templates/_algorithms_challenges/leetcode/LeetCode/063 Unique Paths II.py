"""
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

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
__author__ = 'Danyang'
class Solution:
    ___ uniquePathsWithObstacles(self, obstacleGrid
        """
        dp
        :param obstacleGrid:  a list of lists of integers
        :return: integer
        """
        m = le.(obstacleGrid)
        n = le.(obstacleGrid[0])

        # trivial
        __ obstacleGrid[0][0]__1 or obstacleGrid[m-1][n-1]__1:
            r_ 0

        path = [[0 ___ _ in range(n)] ___ _ in range(m)]  # possible to optimize by [[0 for _ in range(n+1)]]
        path[0][0] = 1 # start

        # path[i][j] = path[i-1][j] + path[i][j-1]
        ___ i in range(m
            ___ j in range(n
                __ i__0 and j__0:
                    continue
                __ i__0:
                    path[i][j] = path[i][j-1] __ obstacleGrid[i][j-1]__0 else 0
                ____ j__0:
                    path[i][j] = path[i-1][j] __ obstacleGrid[i-1][j]__0 else 0
                ____
                    __ obstacleGrid[i][j-1]__0 and obstacleGrid[i-1][j]__0:
                        path[i][j] = path[i-1][j]+path[i][j-1]
                    ____ obstacleGrid[i][j-1]__0:
                        path[i][j] = path[i][j-1]
                    ____ obstacleGrid[i-1][j]__0:
                        path[i][j] = path[i-1][j]
                    ____
                        path[i][j]=0


        r_ path[m-1][n-1]

__ __name____"__main__":
    grid = [[0, 0], [1, 1], [0, 0]]
    assert Solution().uniquePathsWithObstacles(grid)__0

