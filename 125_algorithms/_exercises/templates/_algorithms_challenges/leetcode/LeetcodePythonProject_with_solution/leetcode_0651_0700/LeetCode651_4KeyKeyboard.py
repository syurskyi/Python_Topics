'''
Created on Oct 3, 2017

@author: MT
'''
c_ Solution(o..
    ___ maxA  N
        """
        :type N: int
        :rtype: int
        """
        n = N
        dp = [0]*(n+1)
        ___ i __ r..(1, n+1
            dp[i] = m..(dp[i], i)
            ___ j __ r..(1, n+1
                __ i+j+2 < n+1:
                    dp[i+j+2] = m..(dp[i+j+2], dp[i]*(j+1
        r.. dp[-1]
    
    ___ test
        testCases = [
            1,
            2,
            3,
            7,
        ]
        ___ n __ testCases:
            print('n: %s' % n)
            result = maxA(n)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
