'''
Created on Jun 5, 2018

@author: tongq
'''
class Solution(object):
    ___ isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        __ n.. s and n.. p: r.. True
        m, n = l..(s), l..(p)
        dp = [[False]*(n+1) ___ _ __ r..(m+1)]
        dp[-1][-1] = True
        j = n-1
        while j >= 0 and p[j] __ '*':
            dp[-1][j] = True
            j -= 1
        ___ i __ r..(m-1, -1, -1):
            ___ j __ r..(n-1, -1, -1):
                __ s[i] __ p[j] o. p[j] __ '?':
                    dp[i][j] = dp[i+1][j+1]
                ____ p[j] __ '*':
                    dp[i][j] = dp[i][j+1] o. dp[i+1][j]
        r.. dp[0][0]
