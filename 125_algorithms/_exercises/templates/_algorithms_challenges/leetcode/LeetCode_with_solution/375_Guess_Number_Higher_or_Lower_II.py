c_ Solution o..
    # def getMoneyAmount(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     #top down dp
    #     dp = [[0] * (n + 1) for _ in range(n + 1)]
    #     return self.top_down_dp(dp, 1, n)
    #
    # def top_down_dp(self, dp, begin, end):
    #     if begin >= end:
    #         return 0
    #     if dp[begin][end] != 0:
    #         return dp[begin][end]
    #     res = sys.maxint
    #     for i in xrange(begin, end + 1):
    #         tmp = i + max(self.top_down_dp(dp, begin, i - 1), self.top_down_dp(dp, i + 1, end))
    #         res = min(res, tmp)
    #     dp[begin][end] = res
    #     return res

    ___ getMoneyAmount  n
        # bottom up dp
        # https://discuss.leetcode.com/topic/51353/simple-dp-solution-with-explanation/2
        dp = [[0] * (n + 1) ___ _ __ r.. n + 1)]
        ___ j __ r.. 2, n + 1
            ___ i __ r.. j - 1, 0, -1
                globalMin = sys.maxint
                ___ k __ r.. i + 1, j
                    localMax = k + m..(dp[i][k - 1], dp[k + 1][j])
                    globalMin = min(globalMin, localMax)
                __ i + 1 __ j:
                    dp[i][j] = i
                ____
                    dp[i][j] = globalMin
        r_ dp[1][n]
