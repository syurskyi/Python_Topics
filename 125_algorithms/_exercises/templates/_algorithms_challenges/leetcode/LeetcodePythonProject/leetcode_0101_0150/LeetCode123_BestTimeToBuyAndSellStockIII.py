'''
Created on Feb 6, 2017

@author: MT
'''

class Solution(object
    ___ maxProfit(self, prices
        """
        :type prices: List[int]
        :rtype: int
        """
        __ not prices or le.(prices) <= 1: r_ 0
        left = [0]*le.(prices)
        right = [0]*le.(prices)
        minVal = prices[0]
        ___ i in range(1, le.(prices)):
            left[i] = max(prices[i]-minVal, left[i])
            minVal = min(minVal, prices[i])
        maxVal = prices[-1]
        ___ i in range(le.(prices)-2, -1, -1
            right[i] = max(maxVal-prices[i], right[i+1])
            maxVal = max(maxVal, prices[i])
        profit = 0
        ___ i in range(le.(prices)):
            profit = max(left[i]+right[i], profit)
        r_ profit
    
    ___ test(self
        testCases = [
            [1, 9, 2, 1, 3, 7, 2],
            [1, 7, 2, 9, 3, 1, 10],
            [1, 2],
            [2, 1],
            [3, 3],
        ]
        ___ prices in testCases:
            print('prices: %s' % (prices))
            result = self.maxProfit(prices)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()