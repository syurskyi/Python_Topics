'''
Created on Jan 22, 2017

@author: MT
'''

c_ Solution(o..
    ___ minPathSum  grid
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        __ n.. grid: r.. 0
        n l..(grid 0
        m l..(grid)
        dp [[0]*n ___ i __ r..(m)]
        ___ i __ r..(m
            ___ j __ r..(n
                __ i __ 0 a.. j __ 0:
                    dp[i][j] grid[i][j]
                ____ i __ 0 a.. j !_ 0:
                    dp[i][j] dp[i][j-1] + grid[i][j]
                ____ i !_ 0 a.. j __ 0:
                    dp[i][j] dp[i-1][j] + grid[i][j]
                ____
                    dp[i][j] m..(dp[i-1][j], dp[i][j-1])+grid[i][j]
        r.. dp[-1][-1]
    
    ___ test
        p..

__ _____ __ _____
    Solution().test()