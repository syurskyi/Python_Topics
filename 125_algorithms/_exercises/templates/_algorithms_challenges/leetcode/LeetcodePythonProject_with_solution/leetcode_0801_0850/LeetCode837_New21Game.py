'''
Created on Oct 9, 2018

@author: tongq
'''
c_ Solution(o..
    ___ new21Game  N, K, W
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        n, k, w = N, K, W
        __ k __ 0 o. n >= k+w: r.. 1
        dp = [1.0]+[0.0]*n
        wSum = 1.0
        ___ i __ r..(1, n+1
            dp[i] = wSum/w
            __ i < k: wSum += dp[i]
            __ i - w >= 0: wSum -= dp[i-w]
        r.. s..(dp[k:])
    
    ___ test
        testCases = [
            [10, 1, 10],
            [6, 1, 10],
            [21, 17, 10],
        ]
        ___ n, k, w __ testCases:
            result = new21Game(n, k, w)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
