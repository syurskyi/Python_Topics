'''
Created on May 29, 2018

@author: tongq
'''
c_ Solution(object):
    ___ minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = l..(triangle[-1])
        n = l..(triangle)
        ___ i __ r..(n-2, -1, -1):
            ___ j __ r..(i+1):
                dp[j] = m..(triangle[i][j]+dp[j], triangle[i][j]+dp[j+1])
        r.. dp[0]
