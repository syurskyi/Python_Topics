'''
Created on Jan 22, 2017

@author: MT
'''

class Solution(object):
    ___ minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        __ not grid: return 0
        n = len(grid[0])
        m = len(grid)
        dp = [[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                __ i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0 and j != 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                elif i != 0 and j == 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1])+grid[i][j]
        return dp[-1][-1]
    
    ___ test(self):
        pass

__ __name__ == '__main__':
    Solution().test()