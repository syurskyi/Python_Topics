'''
Created on Feb 6, 2017

@author: MT
'''

c_ Solution(o..):
    ___ maxProfit  prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        __ n.. prices o. l..(prices) <= 1: r.. 0
        left = [0]*l..(prices)
        right = [0]*l..(prices)
        minVal = prices[0]
        ___ i __ r..(1, l..(prices)):
            left[i] = m..(prices[i]-minVal, left[i])
            minVal = m..(minVal, prices[i])
        maxVal = prices[-1]
        ___ i __ r..(l..(prices)-2, -1, -1):
            right[i] = m..(maxVal-prices[i], right[i+1])
            maxVal = m..(maxVal, prices[i])
        profit = 0
        ___ i __ r..(l..(prices)):
            profit = m..(left[i]+right[i], profit)
        r.. profit
    
    ___ test
        testCases = [
            [1, 9, 2, 1, 3, 7, 2],
            [1, 7, 2, 9, 3, 1, 10],
            [1, 2],
            [2, 1],
            [3, 3],
        ]
        ___ prices __ testCases:
            print('prices: %s' % (prices))
            result = maxProfit(prices)
            print('result: %s' % (result))
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()