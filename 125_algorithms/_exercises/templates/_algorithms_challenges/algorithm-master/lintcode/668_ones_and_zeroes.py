"""
optimized space complexity
"""
c_ Solution:
    """
    @param: strs: an array with strings include only 0 and 1
    @param: m: An integer
    @param: n: An integer
    @return: find the maximum number of strings
    """
    ___ findMaxForm  strs, m, n):
        __ n.. strs:
            r.. 0

        """
        `dp[j][k]` means the current str can be made up of
        `j` 0s and `k` 1s
        """
        dp = [[0] * (n + 1) ___ _ __ r..(m + 1)]

        c0 = c1 = 0
        ___ s __ strs:
            c0 = s.c.. '0')
            c1 = l..(s) - c0

            ___ j __ r..(m, c0 - 1, -1):
                ___ k __ r..(n, c1 - 1, -1):
                    """
                    case 1: included current `strs[i - 1]`
                    case 2: not included current `strs[i - 1]`, same as previous
                    """
                    dp[j][k] = m..(
                        dp[j][k],
                        dp[j - c0][k - c1] + 1
                    )

        r.. dp[m][n]


"""
origin
"""
c_ Solution:
    """
    @param: strs: an array with strings include only 0 and 1
    @param: m: An integer
    @param: n: An integer
    @return: find the maximum number of strings
    """
    ___ findMaxForm  strs, m, n):
        __ n.. strs:
            r.. 0

        l = l..(strs)

        """
        `dp[i][j][k]` means the pre- `i`th strs can be made up of
        `j` 0s and `k` 1s

        dp[0][j][k] = 0
        """
        dp = [[[0] * (n + 1) ___ _ __ r..(m + 1)] ___ _ __ r..(l + 1)]

        c0 = c1 = 0
        ___ i __ r..(1, l + 1):
            c0 = strs[i - 1].c.. '0')
            c1 = l..(strs[i - 1]) - c0

            ___ j __ r..(m + 1):
                ___ k __ r..(n + 1):
                    """
                    case 1: included current `strs[i - 1]`
                    """
                    __ j >= c0 a.. k >= c1:
                        dp[i][j][k] = dp[i - 1][j - c0][k - c1] + 1

                    """
                    case 2: not included current `strs[i - 1]`, same as previous
                    """
                    __ dp[i - 1][j][k] > dp[i][j][k]:
                        dp[i][j][k] = dp[i - 1][j][k]

        r.. dp[l][m][n]
