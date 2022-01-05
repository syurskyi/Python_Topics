c_ Solution:
    """
    @param: G: A list of lists of integers
    @return: An integer
    """
    ___ uniquePathsWithObstacles  G):
        __ n.. G o. n.. G[0]:
            r.. 0

        OBSTACLE = 1

        m, n = l..(G), l..(G[0])
        dp = [[0] * n ___ _ __ r..(2)]
        prev = curr = 0

        ___ j __ r..(n):
            __ G[0][j] __ OBSTACLE:
                break
            dp[curr][j] = 1

        ___ i __ r..(1, m):
            prev = curr
            curr = 1 - curr

            dp[curr][0] = 0 __ G[i][0] __ OBSTACLE ____ dp[prev][0]
            ___ j __ r..(1, n):
                __ G[i][j] __ OBSTACLE:
                    dp[curr][j] = 0
                    _____
                dp[curr][j] = dp[prev][j] + dp[curr][j - 1]

        r.. dp[curr][n - 1]
