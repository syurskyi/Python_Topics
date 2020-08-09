'''
Created on Jan 30, 2017

@author: MT
'''
class Solution(object
    ___ numTrees(self, n
        """
        :type n: int
        :rtype: int
        """
        __ n < 1: r_ 1
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        ___ i in range(2, n+1
            ___ j in range(i
                dp[i] += dp[i-j-1]*dp[j]
        r_ dp[-1]
