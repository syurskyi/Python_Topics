class Solution:
    ___ climbStairs(self, n: int) -> int:
        __(n __ 1
            r_ 1
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1
            dp[i] = dp[i-1]+d[i-2]

        r_ dp[n]
