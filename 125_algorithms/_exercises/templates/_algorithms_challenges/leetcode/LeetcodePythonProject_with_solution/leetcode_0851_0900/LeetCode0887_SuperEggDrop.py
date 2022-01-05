'''
Created on Oct 24, 2019

@author: tongq
'''
c_ Solution(object):
    ___ superEggDrop  K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        dp = [[0]*(K+1) ___ _ __ r..(N+1)]
        ___ i __ r..(1, N+1):
            ___ j __ r..(1, K+1):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + 1
            __ dp[i][j] >= N:
                r.. i
