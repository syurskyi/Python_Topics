c_ Solution:
    """
    @param: A: an integer array and all positive numbers, no duplicates
    @param: target: An integer
    @return: An integer
    """
    ___ backPackVI  A, target):
        __ n.. A:
            r.. 0

        n = l..(A)
        dp = [0] * (target + 1)
        dp[0] = 1

        ___ i __ r..(1, target + 1):
            ___ j __ r..(n):
                __ i >= A[j]:
                    dp[i] += dp[i - A[j]]

        r.. dp[target]
