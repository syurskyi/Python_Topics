'''
Created on Mar 18, 2017

@author: MT
'''

c_ Solution(object):
    ___ coinChange  coins, amount):
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        ___ i __ r..(amount+1):
            ___ coin __ coins:
                __ i+coin < amount+1:
                    dp[i+coin] = m..(dp[i+coin], dp[i]+1)
        __ dp[-1] __ float('inf'):
            r.. -1
        r.. dp[-1]
    
    ___ test
        testCases = [
            (
                [1, 2, 5],
                11,
            ),
        ]
        ___ coins, amount __ testCases:
            print('coins: %s' % (coins))
            print('amount: %s' % (amount))
            result = coinChange(coins, amount)
            print('result: %s' % (result))

__ _____ __ _____
    Solution().test()
