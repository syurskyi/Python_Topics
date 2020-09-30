class Solution:
    """
    @param: grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    ___ minPathSum(self, grid
        __ not grid:
            r_ 0

        m, n = le.(grid), le.(grid[0])

        dp = [[0] * n ___ _ __ range(m)]

        ___ j __ range(n
            __ j __ 0:
                dp[0][j] = grid[0][j]
                continue

            dp[0][j] = grid[0][j] + dp[0][j - 1]

        ___ i __ range(1, m
            dp[i][0] = grid[i][0] + dp[i - 1][0]

            ___ j __ range(1, n
                __ dp[i - 1][j] < dp[i][j - 1]:
                    dp[i][j] = grid[i][j] + dp[i - 1][j]
                ____
                    dp[i][j] = grid[i][j] + dp[i][j - 1]

        r_ dp[m - 1][n - 1]
