'''
Created on Apr 1, 2017

@author: MT
'''

class Solution(object
    ___ getMoneyAmount(self, n
        dp = [[0]*(n+1) ___ _ in range(n+1)]
        ___ j in range(2, n+1
            ___ i in range(j-1, 0, -1
                globalMin = float('inf')
                ___ k in range(i+1, j
                    localMax = k+max(dp[i][k-1], dp[k+1][j])
                    globalMin = min(globalMin, localMax)
                __ i+1 __ j:
                    dp[i][j] = i
                ____
                    dp[i][j] = globalMin
        r_ dp[1][n]
    
    ___ test(self
        testCases = [
            10,
        ]
        ___ n in testCases:
            print('n: %s' % n)
            result = self.getMoneyAmount(n)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
