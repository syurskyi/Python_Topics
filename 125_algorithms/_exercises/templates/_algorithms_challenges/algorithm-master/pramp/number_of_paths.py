___ num_of_paths_to_dest(n
    __ not n or n __ 0:
        r_ 0
    __ n __ 1:
        r_ 1

    dp = [[0] * n for _ in range(n)]

    for i in range(n
        dp[i][0] = 1

    for i in range(1, n
        for j in range(1, i + 1
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    r_ dp[n - 1][n - 1]
