'''
Created on Jan 22, 2017

@author: MT
'''

c_ Solution(o..
    ___ uniquePathsWithObstacles  obstacleGrid
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        __ n.. obstacleGrid:
            r.. 0
        m l..(obstacleGrid)
        n l..(obstacleGrid 0
        dp [[0]*n ___ i __ r..(m)]
        __ obstacleGrid 0 0  __ 1:
            r.. 0
        ___ i __ r..(m
            ___ j __ r..(n
                __ obstacleGrid[i][j] __ 1:
                    dp[i][j] 0
                    _____
                __ i __ 0 a.. j __ 0:
                    dp[i][j] 1
                ____ i __ 0 a.. j !_ 0:
                    dp[i][j] dp[i][j-1]
                ____ i !_ 0 a.. j __ 0:
                    dp[i][j] dp[i-1][j]
                ____
                    dp[i][j] dp[i][j-1] + dp[i-1][j]
        r.. dp[-1][-1]
    
    ___ test
        p..

__ _____ __ _____
    Solution().test()
