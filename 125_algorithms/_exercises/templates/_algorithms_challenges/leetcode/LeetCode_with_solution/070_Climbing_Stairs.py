c_ Solution o..
    # def climbStairs(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     dp = [0] * (n + 1)
    #     dp[0] = 1
    #     dp[1] = 1
    #     for i in range(2, n + 1):
    #         dp[i] = dp[i - 2] + dp[i- 1]
    #     return dp[n]

    ___ climbStairs  n):
        __ n <= 1:
            r_ 1
        dp = [1] * 2
        ___ i __ r.. 2, n + 1):
            dp[1], dp[0] = dp[1] + dp[0], dp[1]
        r_ dp[1]



    # C = {1: 1, 2: 2}
    # def climbStairs(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     if n in Solution.C:
    #         return Solution.C[n]
    #     else:
    #         result = Solution.C.get(n - 1, self.climbStairs(n - 1)) + \
    #                  Solution.C.get(n - 2, self.climbStairs(n - 2))
    #         Solution.C[n] = result
    #         return result

