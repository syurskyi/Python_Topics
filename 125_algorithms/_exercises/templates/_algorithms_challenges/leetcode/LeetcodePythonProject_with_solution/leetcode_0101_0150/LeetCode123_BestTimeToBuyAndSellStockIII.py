'''
Created on Feb 6, 2017

@author: MT
'''

c_ Solution(object):
    ___ maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        __ n.. prices o. l..(prices) <= 1: r.. 0
        left = [0]*l..(prices)
        right = [0]*l..(prices)
        minVal = prices[0]
        ___ i __ r..(1, l..(prices)):
            left[i] = max(prices[i]-minVal, left[i])
            minVal = m..(minVal, prices[i])
        maxVal = prices[-1]
        ___ i __ r..(l..(prices)-2, -1, -1):
            right[i] = max(maxVal-prices[i], right[i+1])
            maxVal = max(maxVal, prices[i])
        profit = 0
        ___ i __ r..(l..(prices)):
            profit = max(left[i]+right[i], profit)
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

__ __name__ __ '__main__':
    Solution().test()