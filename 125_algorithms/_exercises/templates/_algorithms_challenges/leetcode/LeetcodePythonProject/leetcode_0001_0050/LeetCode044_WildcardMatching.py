'''
Created on Jun 5, 2018

@author: tongq
'''
class Solution(object
    ___ isMatch(self, s, p
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        __ not s and not p: r_ True
        m, n = le.(s), le.(p)
        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[-1][-1] = True
        j = n-1
        w___ j >= 0 and p[j] __ '*':
            dp[-1][j] = True
            j -= 1
        for i in range(m-1, -1, -1
            for j in range(n-1, -1, -1
                __ s[i] __ p[j] or p[j] __ '?':
                    dp[i][j] = dp[i+1][j+1]
                ____ p[j] __ '*':
                    dp[i][j] = dp[i][j+1] or dp[i+1][j]
        r_ dp[0][0]
