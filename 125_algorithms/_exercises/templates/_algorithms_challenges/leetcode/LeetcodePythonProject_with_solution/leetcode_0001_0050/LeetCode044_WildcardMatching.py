'''
Created on Jun 5, 2018

@author: tongq
'''
c_ Solution(o..
    ___ isMatch  s, p
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        __ n.. s a.. n.. p: r.. T..
        m, n  l..(s), l..(p)
        dp  [[F..]*(n+1) ___ _ __ r..(m+1)]
        dp[-1][-1]  T..
        j  n-1
        w.... j > 0 a.. p[j] __ '*':
            dp[-1][j]  T..
            j - 1
        ___ i __ r..(m-1, -1, -1
            ___ j __ r..(n-1, -1, -1
                __ s[i] __ p[j] o. p[j] __ '?':
                    dp[i][j]  dp[i+1][j+1]
                ____ p[j] __ '*':
                    dp[i][j]  dp[i][j+1] o. dp[i+1][j]
        r.. dp[0][0]
