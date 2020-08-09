'''
Created on Feb 3, 2017

@author: MT
'''

class Solution(object
    ___ numDistinct(self, s, t
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = le.(s), le.(t)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m
            dp[i][0] = 1
        for i in range(m
            for j in range(n
                __ s[i] __ t[j]:
                    dp[i+1][j+1] = dp[i][j] + dp[i][j+1]
                ____
                    dp[i+1][j+1] = dp[i][j+1]
        r_ dp[-1][-1]
    
    ___ test(self
        testCases= [
            ('rabbbit', 'rabbit'),
            ('abbt', 'abt'),
            ('ABCDE', 'ACE'),
            ('ABCDE', 'AEC'),
        ]
        for s, t in testCases:
            print('s: %s, t: %s' % (s, t))
            result = self.numDistinct(s, t)
            print('result: %s' % (result))
            print('-='*20+'-')

Solution().test()