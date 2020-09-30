# Climbing Stairs
# Question: You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Solutions:

class Solution:
    def climbStairs(n):
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for x in range(2, n + 1):
            dp[x] = dp[x - 1] + dp[x - 2]
        return dp[n]

Solution.climbStairs(10)