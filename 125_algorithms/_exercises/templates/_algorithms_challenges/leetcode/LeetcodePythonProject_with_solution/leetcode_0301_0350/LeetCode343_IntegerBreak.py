'''
Created on Mar 20, 2017

@author: MT
'''

c_ Solution(o..
    ___ integerBreak  n
        dp [0]*(n+1)
        ___ i __ r..(1, n
            ___ j __ r..(1, i+1
                __ i+j <_ n:
                    dp[i+j] m..(m..(dp[i], i)*m..(dp[j],j), dp[i+j])
        r.. dp[-1]