c_ Solution:
    """
    @param: grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    ___ minPathSum  grid
        __ n.. grid:
            r.. 0

        m, n = l..(grid), l..(grid[0])

        dp = [[0] * n ___ _ __ r..(m)]

        ___ j __ r..(n
            __ j __ 0:
                dp[0][j] = grid[0][j]
                _____

            dp[0][j] = grid[0][j] + dp[0][j - 1]

        ___ i __ r..(1, m
            dp[i][0] = grid[i][0] + dp[i - 1][0]

            ___ j __ r..(1, n
                __ dp[i - 1][j] < dp[i][j - 1]:
                    dp[i][j] = grid[i][j] + dp[i - 1][j]
                ____:
                    dp[i][j] = grid[i][j] + dp[i][j - 1]

        r.. dp[m - 1][n - 1]
