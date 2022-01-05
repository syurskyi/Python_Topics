'''
Created on Feb 5, 2017

@author: MT
'''
c_ Solution(object):
    ___ maxProfit  prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        __ n.. prices: r.. res
        minVal = prices[0]
        ___ i __ r..(1, l..(prices)):
            res = m..(res, prices[i]-minVal)
            minVal = m..(minVal, prices[i])
        r.. res
    
    ___ test
        testCases = [
            [7, 1, 5, 3, 6, 4],
            [7, 6, 4, 3, 1],
            [2, 4, 1],
        ]
        ___ prices __ testCases:
            print('prices: %s' % (prices))
            result = maxProfit(prices)
            print('result: %s' % (result))
            print('-='*15+'-')
    
__ _____ __ _____
    Solution().test()