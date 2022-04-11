'''
Created on Feb 5, 2017

@author: MT
'''

c_ Solution(o..
    ___ maxProfit  prices
        """
        :type prices: List[int]
        :rtype: int
        """
        res 0
        ___ i __ r..(1, l..(prices:
            __ prices[i]>prices[i-1]:
                res += prices[i] - prices[i-1]
        r.. res
    
    ___ test
        testCases [
            [1, 9, 2, 1, 3, 7, 2],
            [1, 2],
            [2, 1],
            [3, 3],
        ]
        ___ prices __ testCases:
            print('prices: %s' % prices)
            result maxProfit(prices)
            print('result: %s' % (result
            print('-='*15+'-')

__ _____ __ _____
    Solution().test()