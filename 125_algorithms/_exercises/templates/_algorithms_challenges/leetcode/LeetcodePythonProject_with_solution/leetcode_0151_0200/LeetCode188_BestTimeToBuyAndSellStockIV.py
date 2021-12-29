'''
Created on Feb 16, 2017

@author: MT
'''

class Solution(object):
    ___ maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = l..(prices)
        __ k*2 >= n:
            r.. self.quickSolve(prices)
        dp = [[0]*n ___ _ __ r..(k+1)]
        ___ i __ r..(1, k+1):
            tmpMax = -prices[0]
            ___ j __ r..(1, n):
                dp[i][j] = max(dp[i][j-1], tmpMax+prices[j])
                tmpMax = max(tmpMax, dp[i-1][j-1]-prices[j])
        r.. dp[-1][-1]
    
    ___ quickSolve(self, prices):
        res = 0
        ___ i __ r..(1, l..(prices)):
            res += max(0, prices[i]-prices[i-1])
        r.. res
    
    ___ test(self):
        testCases = [
            ([2, 1], 1),
            ([1, 7, 2, 9, 3, 1, 2, 8, 5, 6, 1, 13], 4),
        ]
        ___ prices, k __ testCases:
            print('prices: %s' % (prices))
            print('k: %s' % (k))
            result = self.maxProfit(k, prices)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()