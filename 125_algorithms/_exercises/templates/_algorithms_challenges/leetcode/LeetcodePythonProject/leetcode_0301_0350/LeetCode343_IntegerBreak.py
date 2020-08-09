'''
Created on Mar 20, 2017

@author: MT
'''

class Solution(object
    ___ integerBreak(self, n
        dp = [0]*(n+1)
        ___ i in range(1, n
            ___ j in range(1, i+1
                __ i+j <= n:
                    dp[i+j] = max(max(dp[i], i)*max(dp[j],j), dp[i+j])
        r_ dp[-1]