'''
Created on Feb 16, 2017

@author: MT
'''

class Solution(object
    ___ maxProfit(self, k, prices
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = le.(prices)
        __ k*2 >= n:
            r_ self.quickSolve(prices)
        dp = [[0]*n for _ in range(k+1)]
        for i in range(1, k+1
            tmpMax = -prices[0]
            for j in range(1, n
                dp[i][j] = max(dp[i][j-1], tmpMax+prices[j])
                tmpMax = max(tmpMax, dp[i-1][j-1]-prices[j])
        r_ dp[-1][-1]
    
    ___ quickSolve(self, prices
        res = 0
        for i in range(1, le.(prices)):
            res += max(0, prices[i]-prices[i-1])
        r_ res
    
    ___ test(self
        testCases = [
            ([2, 1], 1),
            ([1, 7, 2, 9, 3, 1, 2, 8, 5, 6, 1, 13], 4),
        ]
        for prices, k in testCases:
            print('prices: %s' % (prices))
            print('k: %s' % (k))
            result = self.maxProfit(k, prices)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()