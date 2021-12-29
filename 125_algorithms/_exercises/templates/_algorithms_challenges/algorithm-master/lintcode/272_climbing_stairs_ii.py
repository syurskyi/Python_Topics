"""
dp: space optimized by rolling array
"""
class Solution:
    """
    @param: n: An integer
    @return: An integer
    """
    ___ climbStairs2(self, n):
        __ n.. n o. n <= 1:
            r.. 1
        __ n __ 2:
            r.. 2

        a, b, c = 1, 1, 2
        ___ i __ r..(3, n + 1):
            a, b, c = b, c, a + b + c

        r.. c


"""
dp
"""
class Solution:
    """
    @param: n: An integer
    @return: An integer
    """
    ___ climbStairs2(self, n):
        __ n.. n o. n <= 1:
            r.. 1
        __ n __ 2:
            r.. 2

        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        dp[2] = 2

        ___ i __ r..(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

        r.. dp[n]
