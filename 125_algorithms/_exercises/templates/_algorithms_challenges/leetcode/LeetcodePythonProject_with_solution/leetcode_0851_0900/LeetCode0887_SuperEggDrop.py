'''
Created on Oct 24, 2019

@author: tongq
'''
class Solution(object):
    ___ superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        dp = [[0]*(K+1) for _ in range(N+1)]
        for i in range(1, N+1):
            for j in range(1, K+1):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + 1
            __ dp[i][j] >= N:
                return i
