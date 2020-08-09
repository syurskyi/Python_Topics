'''
Created on Jan 22, 2017

@author: MT
'''

class Solution(object
    ___ minPathSum(self, grid
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        __ not grid: r_ 0
        n = le.(grid[0])
        m = le.(grid)
        dp = [[0]*n for i in range(m)]
        for i in range(m
            for j in range(n
                __ i __ 0 and j __ 0:
                    dp[i][j] = grid[i][j]
                ____ i __ 0 and j != 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                ____ i != 0 and j __ 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                ____
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1])+grid[i][j]
        r_ dp[-1][-1]
    
    ___ test(self
        pass

__ __name__ __ '__main__':
    Solution().test()