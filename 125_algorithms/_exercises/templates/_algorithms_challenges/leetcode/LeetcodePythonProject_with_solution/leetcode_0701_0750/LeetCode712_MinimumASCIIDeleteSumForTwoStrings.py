'''
Created on Oct 29, 2017

@author: MT
'''
c_ Solution(o..
    ___ minimumDeleteSum  s1, s2
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        n1, n2 = l..(s1), l..(s2)
        dp = [[0]*(n2+1) ___ _ __ r..(n1+1)]
        ___ i __ r..(n1
            dp[i+1][0] = dp[i][0] + o..(s1[i])
        ___ j __ r..(n2
            dp[0][j+1] = dp[0][j] + o..(s2[j])
        ___ i __ r..(n1
            ___ j __ r..(n2
                __ s1[i] __ s2[j]:
                    dp[i+1][j+1] = dp[i][j]
                ____:
                    dp[i+1][j+1] = m..(dp[i+1][j]+o..(s2[j]), dp[i][j+1]+o..(s1[i]))
        r.. dp[-1][-1]
    
    ___ test
        testCases = [
            [
                'sea',
                'eat',
            ],
            [
                'delete',
                'leet',
            ],
        ]
        ___ s1, s2 __ testCases:
            print('s1: %s' % s1)
            print('s2: %s' % s2)
            result = minimumDeleteSum(s1, s2)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
