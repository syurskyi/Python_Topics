class Solution:
    """
    @param: G: A list of lists of integers
    @return: An integer
    """
    ___ uniquePathsWithObstacles(self, G):
        __ not G or not G[0]:
            return 0

        OBSTACLE = 1

        m, n = len(G), len(G[0])
        dp = [[0] * n for _ in range(2)]
        prev = curr = 0

        for j in range(n):
            __ G[0][j] == OBSTACLE:
                break
            dp[curr][j] = 1

        for i in range(1, m):
            prev = curr
            curr = 1 - curr

            dp[curr][0] = 0 __ G[i][0] == OBSTACLE else dp[prev][0]
            for j in range(1, n):
                __ G[i][j] == OBSTACLE:
                    dp[curr][j] = 0
                    continue
                dp[curr][j] = dp[prev][j] + dp[curr][j - 1]

        return dp[curr][n - 1]
