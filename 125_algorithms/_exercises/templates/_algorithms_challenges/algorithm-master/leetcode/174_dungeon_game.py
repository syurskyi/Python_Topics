c_ Solution:
    ___ calculateMinimumHP  G
        """
        :type G: List[List[int]]
        :rtype: int
        """
        INFINITY f__('inf')
        m, n l..(G), l..(G 0
        dp [[INFINITY] * (n + 1) ___ _ __ r..(m + 1)]
        dp[m][n - 1] 1
        dp[m - 1][n] 1

        ___ i __ r..(m - 1, -1, -1
            ___ j __ r..(n - 1, -1, -1
                dp[i][j] m..(dp[i + 1][j], dp[i][j + 1]) - G[i][j]
                __ dp[i][j] <_ 0:
                    dp[i][j] 1

        r.. dp 0 0 
