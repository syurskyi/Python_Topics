'''
Created on May 29, 2018

@author: tongq
'''
class Solution(object
    ___ minimumTotal(self, triangle
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = list(triangle[-1])
        n = le.(triangle)
        ___ i in range(n-2, -1, -1
            ___ j in range(i+1
                dp[j] = min(triangle[i][j]+dp[j], triangle[i][j]+dp[j+1])
        r_ dp[0]
