'''
Created on Mar 18, 2017

@author: MT
'''

class Solution(object
    ___ coinChange(self, coins, amount
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        ___ i __ range(amount+1
            ___ coin __ coins:
                __ i+coin < amount+1:
                    dp[i+coin] = min(dp[i+coin], dp[i]+1)
        __ dp[-1] __ float('inf'
            r_ -1
        r_ dp[-1]
    
    ___ test(self
        testCases = [
            (
                [1, 2, 5],
                11,
            ),
        ]
        ___ coins, amount __ testCases:
            print('coins: %s' % (coins))
            print('amount: %s' % (amount))
            result = self.coinChange(coins, amount)
            print('result: %s' % (result))

__  -n __ '__main__':
    Solution().test()
