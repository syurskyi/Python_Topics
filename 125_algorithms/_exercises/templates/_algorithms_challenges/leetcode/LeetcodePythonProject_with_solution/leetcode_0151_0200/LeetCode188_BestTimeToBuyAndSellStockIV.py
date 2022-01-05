'''
Created on Feb 16, 2017

@author: MT
'''

c_ Solution(object):
    ___ maxProfit  k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = l..(prices)
        __ k*2 >= n:
            r.. quickSolve(prices)
        dp = [[0]*n ___ _ __ r..(k+1)]
        ___ i __ r..(1, k+1):
            tmpMax = -prices[0]
            ___ j __ r..(1, n):
                dp[i][j] = m..(dp[i][j-1], tmpMax+prices[j])
                tmpMax = m..(tmpMax, dp[i-1][j-1]-prices[j])
        r.. dp[-1][-1]
    
    ___ quickSolve  prices):
        res = 0
        ___ i __ r..(1, l..(prices)):
            res += m..(0, prices[i]-prices[i-1])
        r.. res
    
    ___ test
        testCases = [
            ([2, 1], 1),
            ([1, 7, 2, 9, 3, 1, 2, 8, 5, 6, 1, 13], 4),
        ]
        ___ prices, k __ testCases:
            print('prices: %s' % (prices))
            print('k: %s' % (k))
            result = maxProfit(k, prices)
            print('result: %s' % (result))
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()