'''
Created on Jan 22, 2017

@author: MT
'''

class Solution(object
    ___ uniquePaths(self, m, n
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0]*n ___ _ in range(m)]
        ___ i in range(m
            dp[i][0] = 1
        ___ j in range(n
            dp[0][j] = 1
        ___ i in range(1, m
            ___ j in range(1, n
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        r_ dp[-1][-1]
    
    ___ uniquePaths_orig(self, m, n
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        __ m <= 0 or n <= 0: r_ 0
        dp  = [[0]*m ___ i in range(n)]
        dp[0][0] = 1
        ___ i in range(0, n
            ___ j in range(0, m
                __ i __ 0 and j __ 0:
                    dp[i][j] = 1
                ____ i __ 0:
                    dp[i][j] = dp[i][j-1]
                ____ j __ 0:
                    dp[i][j] = dp[i-1][j]
                ____
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        r_ dp[-1][-1]
    
    ___ test(self
        pass

__ __name__ __ '__main__':
    pass