'''
Created on Feb 5, 2017

@author: MT
'''
class Solution(object):
    ___ maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        __ not prices: return res
        minVal = prices[0]
        for i in range(1, len(prices)):
            res = max(res, prices[i]-minVal)
            minVal = min(minVal, prices[i])
        return res
    
    ___ test(self):
        testCases = [
            [7, 1, 5, 3, 6, 4],
            [7, 6, 4, 3, 1],
            [2, 4, 1],
        ]
        for prices in testCases:
            print('prices: %s' % (prices))
            result = self.maxProfit(prices)
            print('result: %s' % (result))
            print('-='*15+'-')
    
__ __name__ == '__main__':
    Solution().test()