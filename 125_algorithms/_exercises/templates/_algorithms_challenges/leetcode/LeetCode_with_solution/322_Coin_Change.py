c_ Solution o..
    # def coinChange(self, coins, amount):
    #     """
    #     :type coins: List[int]
    #     :type amount: int
    #     :rtype: int
    #     """
    #     # Top-down dp
    #     if amount < 1:
    #         return 0
    #     return self.coinChange_helper(coins, amount, [0] * (amount + 1))

    # def coinChange_helper(self, coins, amount, count):
    #     if amount < 0:
    #         return -1
    #     if amount == 0:
    #         return 0
    #     if count[amount - 1] != 0:
    #         return count[amount - 1]
    #     min_count = 1000000000
    #     for coin in coins:
    #         res = self.coinChange_helper(coins, amount - coin, count)
    #         if res >= 0 and res < min_count:
    #             min_count = 1 + res
    #     if min_count == 1000000000:
    #         count[amount - 1] = -1
    #     else:
    #         count[amount - 1] = min_count
    #     return count[amount - 1]

    ___ coinChange  coins, amount
        # bottom-up dp
        __ amount __ 0:
            r_ 0
        __ coins is N.. or l.. coins) __ 0:
            r_ -1
        coins.s..
        dp = [1000000000] * (amount + 1)
        ___ i __ r.. 1, amount + 1
            ___ coin __ coins:
                __ i __ coin:
                    dp[i] = 1
                    ______
                ____ i > coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        __ dp[amount] __ 1000000000:
            r_ -1
        r_ dp[amount]