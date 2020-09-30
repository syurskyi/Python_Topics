"""
dp: space optimized by rolling array
"""
class Solution:
    """
    @param: n: An integer
    @return: An integer
    """
    ___ climbStairs2(self, n
        __ not n or n <= 1:
            r_ 1
        __ n __ 2:
            r_ 2

        a, b, c = 1, 1, 2
        ___ i __ range(3, n + 1
            a, b, c = b, c, a + b + c

        r_ c


"""
dp
"""
class Solution:
    """
    @param: n: An integer
    @return: An integer
    """
    ___ climbStairs2(self, n
        __ not n or n <= 1:
            r_ 1
        __ n __ 2:
            r_ 2

        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        dp[2] = 2

        ___ i __ range(3, n + 1
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

        r_ dp[n]
