'''
Created on Mar 18, 2017

@author: MT
'''

class Solution(object):
    ___ coinChange(self, coins, amount):
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for i in range(amount+1):
            for coin in coins:
                __ i+coin < amount+1:
                    dp[i+coin] = min(dp[i+coin], dp[i]+1)
        __ dp[-1] == float('inf'):
            return -1
        return dp[-1]
    
    ___ test(self):
        testCases = [
            (
                [1, 2, 5],
                11,
            ),
        ]
        for coins, amount in testCases:
            print('coins: %s' % (coins))
            print('amount: %s' % (amount))
            result = self.coinChange(coins, amount)
            print('result: %s' % (result))

__ __name__ == '__main__':
    Solution().test()
