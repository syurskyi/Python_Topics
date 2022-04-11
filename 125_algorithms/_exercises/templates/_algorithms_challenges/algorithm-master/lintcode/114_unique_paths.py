c_ Solution:
    ___ uniquePaths  m, n
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp [[1] * n ___ _ __ r..(m)]

        ___ x __ r..(1, m
            ___ y __ r..(1, n
                dp[x][y] dp[x - 1][y] + dp[x][y - 1]

        r.. dp[m - 1][n - 1]
