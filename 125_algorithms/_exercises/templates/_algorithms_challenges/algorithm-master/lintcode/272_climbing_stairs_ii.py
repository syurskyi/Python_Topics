"""
dp: space optimized by rolling array
"""
class Solution:
    """
    @param: n: An integer
    @return: An integer
    """
    ___ climbStairs2(self, n):
        __ not n or n <= 1:
            return 1
        __ n == 2:
            return 2

        a, b, c = 1, 1, 2
        for i in range(3, n + 1):
            a, b, c = b, c, a + b + c

        return c


"""
dp
"""
class Solution:
    """
    @param: n: An integer
    @return: An integer
    """
    ___ climbStairs2(self, n):
        __ not n or n <= 1:
            return 1
        __ n == 2:
            return 2

        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

        return dp[n]
