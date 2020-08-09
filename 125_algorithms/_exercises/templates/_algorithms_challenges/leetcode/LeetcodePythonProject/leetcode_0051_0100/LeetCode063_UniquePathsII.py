'''
Created on Jan 22, 2017

@author: MT
'''

class Solution(object
    ___ uniquePathsWithObstacles(self, obstacleGrid
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        __ not obstacleGrid:
            r_ 0
        m = le.(obstacleGrid)
        n = le.(obstacleGrid[0])
        dp = [[0]*n for i in range(m)]
        __ obstacleGrid[0][0] __ 1:
            r_ 0
        for i in range(m
            for j in range(n
                __ obstacleGrid[i][j] __ 1:
                    dp[i][j] = 0
                    continue
                __ i __ 0 and j __ 0:
                    dp[i][j] = 1
                ____ i __ 0 and j != 0:
                    dp[i][j] = dp[i][j-1]
                ____ i != 0 and j __ 0:
                    dp[i][j] = dp[i-1][j]
                ____
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
        r_ dp[-1][-1]
    
    ___ test(self
        pass

__ __name__ __ '__main__':
    Solution().test()
