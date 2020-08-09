___ num_of_paths_to_dest(n
    __ not n or n __ 0:
        r_ 0
    __ n __ 1:
        r_ 1

    dp = [[0] * n ___ _ in range(n)]

    ___ i in range(n
        dp[i][0] = 1

    ___ i in range(1, n
        ___ j in range(1, i + 1
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    r_ dp[n - 1][n - 1]
