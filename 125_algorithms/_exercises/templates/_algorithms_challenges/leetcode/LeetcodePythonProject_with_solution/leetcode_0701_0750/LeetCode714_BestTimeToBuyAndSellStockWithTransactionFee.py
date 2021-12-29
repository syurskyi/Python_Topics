'''
Created on Oct 29, 2017

@author: MT
'''
class Solution(object):
    ___ maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        __ n.. prices: r.. 0
        n = l..(prices)
        buy = [0]*n
        sell = [0]*n
        buy[0] = -prices[0]
        ___ i __ r..(1, n):
            buy[i] = max(buy[i-1], sell[i-1]-prices[i])
            sell[i] = max(sell[i-1], buy[i-1]+prices[i]-fee)
        r.. max(buy[-1], sell[-1])
    
    ___ test(self):
        testCases = [
            [
                [1, 3, 2, 8, 4, 9],
                2,
            ],
            [
                [1, 3, 7, 5, 10, 3],
                3,
            ],
        ]
        ___ prices, fee __ testCases:
            print('prices: %s' % prices)
            print('fee: %s' % fee)
            result = self.maxProfit(prices, fee)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
