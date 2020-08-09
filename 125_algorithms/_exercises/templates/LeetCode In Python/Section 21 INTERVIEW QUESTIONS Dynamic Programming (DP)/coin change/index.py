class Solution:
    ___ coinChange(self, coins: List[int], amount: int) -> int:
        __ amount <= 0:
            r_ 0
        
        __ min(coins) > amount:
            r_ -1

        INT_MAX = 1<<32
        dp = [INT_MAX] * (amount +1)
        
        dp[0] = 0
        
        ___ i __ ra..(1, amount + 1
            ___ coin __ coins:
                __ coin <= i:
                    dp[i] = min((dp[i-coin] + 1), dp[i])
                    
        r_ dp[amount] __ dp[amount] != INT_MAX else -1