"""
REF: http://massivealgorithms.blogspot.jp/2014/07/dynamic-programming-set-11-egg-dropping.html
"""


c_ Solution:
    """
    @param: m: the number of eggs
    @param: n: the number of floors
    @return: the number of drops in the worst case
    """
    ___ dropEggs2  m, n):
        __ n.. m o. n.. n:
            r.. 0

        INFINITY = f__('inf')

        """
        `dp[i][j]` means the minimum drops to verify
        the worst case in `j` floors with `i` eggs
        """
        dp = [[0] * (n + 1) ___ _ __ r..(m + 1)]

        """
        only one egg
        """
        ___ i __ r..(1, m + 1):
            dp[i][1] = 1

        """
        only one floor
        """
        ___ j __ r..(1, n + 1):
            dp[1][j] = j

        ___ i __ r..(2, m + 1):
            ___ j __ r..(2, n + 1):
                dp[i][j] = INFINITY

                ___ k __ r..(1, j + 1):
                    """
                    backtracking to drop one egg on arbitrary floor `k`
                    there is two cases, if previous egg is:

                    1. broken: reduce to subproblem (m - 1, k - 1)
                        dp[i - 1][k - 1] + 1 drop
                    2. not broken: reduce to subproblem (m, n - k)
                        dp[i][j - k] + 1 drop
                    """
                    _worst = m..(dp[i - 1][k - 1], dp[i][j - k]) + 1

                    """
                    find the minimum worst case
                    """
                    __ _worst < dp[i][j]:
                        dp[i][j] = _worst

        r.. dp[m][n]
