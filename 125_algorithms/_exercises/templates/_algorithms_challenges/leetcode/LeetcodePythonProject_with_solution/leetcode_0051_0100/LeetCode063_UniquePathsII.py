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
        __ n.. obstacleGrid:
            r.. 0
        m = l..(obstacleGrid)
        n = l..(obstacleGrid[0])
        dp = [[0]*n ___ i __ r..(m)]
        __ obstacleGrid[0][0] __ 1:
            r.. 0
        ___ i __ r..(m):
            ___ j __ r..(n):
                __ obstacleGrid[i][j] __ 1:
                    dp[i][j] = 0
                    continue
                __ i __ 0 and j __ 0:
                    dp[i][j] = 1
                ____ i __ 0 and j != 0:
                    dp[i][j] = dp[i][j-1]
                ____ i != 0 and j __ 0:
                    dp[i][j] = dp[i-1][j]
                ____:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
        r.. dp[-1][-1]
    
    ___ test(self):
        pass

__ __name__ __ '__main__':
    Solution().test()
