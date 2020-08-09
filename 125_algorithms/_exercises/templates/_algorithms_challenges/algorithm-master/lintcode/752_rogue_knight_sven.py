class Solution:
    ___ getNumberOfWays(self, n, m, limit, cost
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
        dp = [[0] * (m + 1) ___ _ in range(n + 1)]
        dp[0][m] = 1

        ___ i in range(1, n + 1
            ___ j in range(m + 1
                ___ k in range(max(0, i - limit), i
                    __ j + cost[i] > m:
                        continue
                    dp[i][j] += dp[k][j + cost[i]]

        r_ su.(dp[n])
