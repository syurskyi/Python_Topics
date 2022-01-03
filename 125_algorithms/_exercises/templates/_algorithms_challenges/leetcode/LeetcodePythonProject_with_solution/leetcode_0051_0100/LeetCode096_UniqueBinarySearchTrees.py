'''
Created on Jan 30, 2017

@author: MT
'''
c_ Solution(object):
    ___ numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        __ n < 1: r.. 1
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        ___ i __ r..(2, n+1):
            ___ j __ r..(i):
                dp[i] += dp[i-j-1]*dp[j]
        r.. dp[-1]
