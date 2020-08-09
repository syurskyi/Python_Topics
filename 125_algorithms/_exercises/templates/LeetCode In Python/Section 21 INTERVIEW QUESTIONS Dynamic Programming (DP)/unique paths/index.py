c_ Solution:
    ___ uniquePaths(, m: int, n: int) -> int:
        
        dp _ [[0 ___ x __ ra..(m)] ___ y __ ra..(n)]
        ___ i __ ra..(m
            dp[0][i] _ 1
        
        ___ i __ ra..(n
            dp[i][0] _ 1
        
        ___ i __ ra..(1, n
            ___ j __ ra..(1, m
                dp[i][j] _ dp[i-1][j] + dp[i][j-1]
        
        r_(dp[-1][-1])