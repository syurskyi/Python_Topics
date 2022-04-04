'''
Created on Mar 5, 2017

@author: MT
'''

c_ Solution(o..
    ___ numSquares  n
        """
        :type n: int
        :rtype: int
        """
        _______ m__
        maxVal = i..(m__.sqrt(n+1
        __ n < 0: r.. 0
        dp = [f__('inf')]*(n+1)
        dp[0] = 0
        dp[1] = 1
        ___ i __ r..(n+1
            ___ j __ r..(maxVal
                __ j*j<=i:
                    dp[i] = m..(dp[i], dp[i-j*j]+1)
        r.. dp[-1]
    
    ___ test
        testCases = [
            12,
            13,
            24,
        ]
        ___ n __ testCases:
            print('n: %s' % (n
            result = numSquares(n)
            print('result: %s' % (result
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()
