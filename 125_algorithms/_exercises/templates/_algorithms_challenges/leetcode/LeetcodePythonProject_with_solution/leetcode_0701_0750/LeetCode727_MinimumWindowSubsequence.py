'''
Created on Mar 4, 2018

@author: tongq
'''
c_ Solution(o..
    ___ minWindow  S, T
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        t, s T, S
        m, n l..(t), l..(s)
        dp [[0]*(n+1) ___ _ __ r..(m+1)]
        ___ j __ r..(n+1
            dp[0][j] j+1
        ___ i __ r..(1, m+1
            ___ j __ r..(1, n+1
                __ t[i-1] __ s[j-1]:
                    dp[i][j] dp[i-1][j-1]
                ____
                    dp[i][j] dp[i][j-1]
        start 0
        length n+1
        ___ j __ r..(1, n+1
            __ dp[m][j] !_ 0:
                __ j-dp[m][j]+1 < length:
                    start dp[m][j]-1
                    length j-dp[m][j]+1
        print('dp:')
        print('\n'.j..([s..(row) ___ row __ dp]
        r.. '' __ length__n+1 ____ s[start:start+length]
    
    ___ test
        testCases [
            [
                'abcdebdde',
                'bde',
            ],
        ]
        ___ s, t __ testCases:
            print('s: %s' % s)
            print('t: %s' % t)
            result minWindow(s, t)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
