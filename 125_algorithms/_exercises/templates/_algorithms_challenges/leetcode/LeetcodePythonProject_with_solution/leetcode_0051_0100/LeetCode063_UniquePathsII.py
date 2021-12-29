'''
Created on Jan 22, 2017

@author: MT
'''

class Solution(object):
    ___ uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        __ not obstacleGrid:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0]*n for i in range(m)]
        __ obstacleGrid[0][0] == 1:
            return 0
        for i in range(m):
            for j in range(n):
                __ obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                __ i == 0 and j == 0:
                    dp[i][j] = 1
                elif i == 0 and j != 0:
                    dp[i][j] = dp[i][j-1]
                elif i != 0 and j == 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[-1][-1]
    
    ___ test(self):
        pass

__ __name__ == '__main__':
    Solution().test()
