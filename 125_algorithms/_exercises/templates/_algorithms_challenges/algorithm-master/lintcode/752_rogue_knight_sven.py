c_ Solution:
    ___ getNumberOfWays  n, m, limit, cost):
        """
        :type n: int
        :type m: int
        :type limit: int
        :type cost: List[int]
        :rtype: int
        """

        """
        `dp[i][j]` means the ways to reach planet `i` and still keep `j` coins
        """
        dp = [[0] * (m + 1) ___ _ __ r..(n + 1)]
        dp[0][m] = 1

        ___ i __ r..(1, n + 1):
            ___ j __ r..(m + 1):
                ___ k __ r..(m..(0, i - limit), i):
                    __ j + cost[i] > m:
                        _____
                    dp[i][j] += dp[k][j + cost[i]]

        r.. s..(dp[n])
