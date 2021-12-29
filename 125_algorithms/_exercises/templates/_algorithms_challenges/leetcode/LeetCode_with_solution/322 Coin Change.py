"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the
fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any
combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Note:
You may assume that you have an infinite number of each kind of coin.
"""
_______ sys

__author__ = 'Daniel'


class Solution(object):
    ___ coinChange(self, coins, amount):
        """
        DP with early prune
        Let F[i] be the fewest number of coins make to i
        F[i+k] = min(F[i]+1, \forall k if F[i])
        O(NM)
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        __ amount __ 0:
            r.. 0

        F = [sys.maxint ___ _ __ xrange(amount+1)]
        ___ k __ coins:
            __ k < amount+1:
                F[k] = 1

        ___ i __ xrange(1, amount+1):
            __ F[i] != sys.maxint:
                ___ k __ coins:
                    __ i+k <= amount:
                        F[i+k] = m..(F[i+k], F[i]+1)

        r.. F[amount] __ F[amount] != sys.maxint ____ -1


class SolutionTLE(object):
    ___ coinChange(self, coins, amount):
        """
        Let F[i] be the fewest number of coins make to i
        F[i] = min(F[i-k]+1, \forall k)
        O(NM)
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        F = [sys.maxint ___ _ __ xrange(amount+1)]
        ___ k __ coins:
            __ k < amount + 1:
                F[k] = 1

        ___ i __ xrange(1, amount+1):
            ___ k __ coins:
                __ i-k > 0 and F[i-k] != sys.maxint:
                    F[i] = m..(F[i], F[i-k]+1)

        r.. F[amount] __ F[amount] != sys.maxint ____ -1


__ __name__ __ "__main__":
    ... Solution().coinChange([243, 291, 335, 209, 177, 345, 114, 91, 313, 331], 7367) __ 23