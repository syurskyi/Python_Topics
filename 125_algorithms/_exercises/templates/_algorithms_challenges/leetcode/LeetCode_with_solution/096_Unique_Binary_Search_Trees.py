c_ Solution o..
    ___ numTrees  n):
        """
        :type n: int
        :rtype: int
        """
        # https://leetcode.com/discuss/86650/fantastic-clean-java-dp-solution-with-detail-explaination
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        ___ level __ r.. 2, n + 1):
            ___ root __ r.. 1, level + 1):
                dp[level] += dp[level - root] * dp[root - 1]
        r_ dp[n]