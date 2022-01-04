c_ Solution:
    """
    @param m: the rows of matrix
    @param n: the cols of matrix
    @param P: the bad computers
    @return: The answer
    """
    ___ maintenance(self, m, n, P):
        __ n.. m o. n.. n o. n.. P:
            r.. 0

        dp = [[0, 0] ___ _ __ r..(m)]
        G = [[0] * n ___ _ __ r..(m)]

        ___ p __ P:
            G[p.x][p.y] = 1

        ___ i __ r..(m):
            left = right = -1

            ___ j __ r..(n):
                __ G[i][j] __ 0:
                    _____
                left = max(left, n - 1 - j)
                right = max(right, j)

            __ i __ 0:
                __ right __ -1:
                    dp[i][0] = 0
                    dp[i][1] = n - 1
                ____:
                    dp[i][0] = 2 * right
                    dp[i][1] = n - 1
            ____:
                __ right __ -1:
                    dp[i][0] = dp[i - 1][0] + 1
                    dp[i][1] = dp[i - 1][1] + 1
                ____:
                    dp[i][0] = 1 + m..(
                        dp[i - 1][0] + 2 * right,
                        dp[i - 1][1] + n - 1
                    )
                    dp[i][1] = 1 + m..(
                        dp[i - 1][1] + 2 * left,
                        dp[i - 1][0] + n - 1
                    )

        r.. m..(dp[m - 1][0], dp[m - 1][1])
