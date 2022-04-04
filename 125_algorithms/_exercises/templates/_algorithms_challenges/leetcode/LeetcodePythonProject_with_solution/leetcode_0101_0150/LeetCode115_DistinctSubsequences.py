'''
Created on Feb 3, 2017

@author: MT
'''

c_ Solution(o..
    ___ numDistinct  s, t
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = l..(s), l..(t)
        dp = [[0]*(n+1) ___ _ __ r..(m+1)]
        ___ i __ r..(m
            dp[i][0] = 1
        ___ i __ r..(m
            ___ j __ r..(n
                __ s[i] __ t[j]:
                    dp[i+1][j+1] = dp[i][j] + dp[i][j+1]
                ____:
                    dp[i+1][j+1] = dp[i][j+1]
        r.. dp[-1][-1]
    
    ___ test
        testCases= [
            ('rabbbit', 'rabbit'),
            ('abbt', 'abt'),
            ('ABCDE', 'ACE'),
            ('ABCDE', 'AEC'),
        ]
        ___ s, t __ testCases:
            print('s: %s, t: %s' % (s, t
            result = numDistinct(s, t)
            print('result: %s' % (result
            print('-='*20+'-')

Solution().test()