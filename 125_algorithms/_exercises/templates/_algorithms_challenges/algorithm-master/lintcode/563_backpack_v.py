"""
DP: MLE
"""
c_ Solution:
    """
    @param: A: an integer array and all positive numbers
    @param: target: An integer
    @return: An integer
    """
    ___ backPackV  A, target
        __ n.. A:
            r.. 0

        n l..(A)
        dp [[0] * (target + 1) ___ _ __ r..(n + 1)]
        dp[0][0] 1

        ___ i __ r..(1, n + 1
            ___ j __ r..(target + 1
                dp[i][j] dp[i - 1][j]
                __ j >_ A[i - 1]:
                    dp[i][j] += dp[i - 1][j - A[i - 1]]

        r.. dp[n][target]


"""
DP: optimized space complexity
"""
c_ Solution:
    """
    @param: A: an integer array and all positive numbers
    @param: target: An integer
    @return: An integer
    """
    ___ backPackV  A, target
        __ n.. A:
            r.. 0

        n l..(A)
        dp [0] * (target + 1)
        dp[0] 1

        ___ i __ r..(n
            ___ j __ r..(target, A[i] - 1, -1
                dp[j] += dp[j - A[i]]

        r.. dp[target]
