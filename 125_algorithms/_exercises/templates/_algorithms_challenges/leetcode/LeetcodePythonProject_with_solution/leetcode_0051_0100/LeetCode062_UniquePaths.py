'''
Created on Jan 22, 2017

@author: MT
'''

class Solution(object):
    ___ uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0]*n ___ _ __ r..(m)]
        ___ i __ r..(m):
            dp[i][0] = 1
        ___ j __ r..(n):
            dp[0][j] = 1
        ___ i __ r..(1, m):
            ___ j __ r..(1, n):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        r.. dp[-1][-1]
    
    ___ uniquePaths_orig(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        __ m <= 0 o. n <= 0: r.. 0
        dp  = [[0]*m ___ i __ r..(n)]
        dp[0][0] = 1
        ___ i __ r..(0, n):
            ___ j __ r..(0, m):
                __ i __ 0 a.. j __ 0:
                    dp[i][j] = 1
                ____ i __ 0:
                    dp[i][j] = dp[i][j-1]
                ____ j __ 0:
                    dp[i][j] = dp[i-1][j]
                ____:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        r.. dp[-1][-1]
    
    ___ test(self):
        pass

__ __name__ __ '__main__':
    pass