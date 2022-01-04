'''
Created on May 5, 2017

@author: MT
'''
c_ Solution(object):
    ___ isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = l..(s), l..(p)
        dp = [[F..]*(n+1) ___ _ __ r..(m+1)]
        dp[0][0] = T..
        ___ j __ r..(n):
            __ p[j] __ '*' a.. dp[0][j-1]:
                dp[0][j+1] = T..
        ___ i __ r..(m):
            ___ j __ r..(n):
                __ s[i] __ p[j] o. p[j] __ '.':
                    dp[i+1][j+1] = dp[i][j]
                ____ p[j] __ '*':
                    __ p[j-1] __ '.' o. s[i] __ p[j-1]:
                        dp[i+1][j+1] = dp[i][j+1] o. dp[i+1][j-1]
                    ____:
                        dp[i+1][j+1] = dp[i+1][j-1]
        r.. dp[-1][-1]
    
    ___ test
        testCases = [
            ['aa', 'a'],
            ['aa', 'a*'],
            ['ab', '.*'],
            ['aab', 'c*a*b'],
            ['mississippi', 'mis*is*p*.'],
        ]
        ___ s, p __ testCases:
            print('s: %s' % s)
            print('p: %s' % p)
            result = isMatch(s, p)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
