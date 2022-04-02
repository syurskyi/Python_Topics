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
c_ Solution:
    ___ uniquePathsWithObstacles  obstacleGrid
        """
        dp
        :param obstacleGrid:  a list of lists of integers
        :return: integer
        """
        m = l..(obstacleGrid)
        n = l..(obstacleGrid[0])

        # trivial
        __ obstacleGrid[0][0]__1 o. obstacleGrid[m-1][n-1]__1:
            r.. 0

        p.. = [[0 ___ _ __ r..(n)] ___ _ __ r..(m)]  # possible to optimize by [[0 for _ in range(n+1)]]
        p..[0][0] = 1 # start

        # path[i][j] = path[i-1][j] + path[i][j-1]
        ___ i __ r..(m
            ___ j __ r..(n
                __ i__0 a.. j__0:
                    _____
                __ i__0:
                    p..[i][j] = p..[i][j-1] __ obstacleGrid[i][j-1]__0 ____ 0
                ____ j__0:
                    p..[i][j] = p..[i-1][j] __ obstacleGrid[i-1][j]__0 ____ 0
                ____:
                    __ obstacleGrid[i][j-1]__0 a.. obstacleGrid[i-1][j]__0:
                        p..[i][j] = p..[i-1][j]+p..[i][j-1]
                    ____ obstacleGrid[i][j-1]__0:
                        p..[i][j] = p..[i][j-1]
                    ____ obstacleGrid[i-1][j]__0:
                        p..[i][j] = p..[i-1][j]
                    ____:
                        p..[i][j]=0


        r.. p..[m-1][n-1]

__ _____ __ ____
    grid = [[0, 0], [1, 1], [0, 0]]
    ... Solution().uniquePathsWithObstacles(grid)__0

