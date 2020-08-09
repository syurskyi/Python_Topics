'''
Created on Oct 24, 2019

@author: tongq
'''
class Solution(object
    ___ superEggDrop(self, K, N
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        dp = [[0]*(K+1) ___ _ in range(N+1)]
        ___ i in range(1, N+1
            ___ j in range(1, K+1
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + 1
            __ dp[i][j] >= N:
                r_ i
