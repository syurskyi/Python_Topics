class Solution:
    """
    @param m: the rows of matrix
    @param n: the cols of matrix
    @param P: the bad computers
    @return: The answer
    """
    ___ maintenance(self, m, n, P
        __ not m or not n or not P:
            r_ 0

        dp = [[0, 0] ___ _ in range(m)]
        G = [[0] * n ___ _ in range(m)]

        ___ p in P:
            G[p.x][p.y] = 1

        ___ i in range(m
            left = right = -1

            ___ j in range(n
                __ G[i][j] __ 0:
                    continue
                left = max(left, n - 1 - j)
                right = max(right, j)

            __ i __ 0:
                __ right __ -1:
                    dp[i][0] = 0
                    dp[i][1] = n - 1
                ____
                    dp[i][0] = 2 * right
                    dp[i][1] = n - 1
            ____
                __ right __ -1:
                    dp[i][0] = dp[i - 1][0] + 1
                    dp[i][1] = dp[i - 1][1] + 1
                ____
                    dp[i][0] = 1 + min(
                        dp[i - 1][0] + 2 * right,
                        dp[i - 1][1] + n - 1
                    )
                    dp[i][1] = 1 + min(
                        dp[i - 1][1] + 2 * left,
                        dp[i - 1][0] + n - 1
                    )

        r_ min(dp[m - 1][0], dp[m - 1][1])
