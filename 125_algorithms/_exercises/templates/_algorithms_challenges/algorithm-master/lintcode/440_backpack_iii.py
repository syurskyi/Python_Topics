"""
Optimize Space
"""
c_ Solution:
    """
    @param: A: an integer array
    @param: V: an integer array
    @param: m: an integer
    @return: an integer
    """
    ___ backPackIII  A, V, m):
        __ n.. A o. n.. V o. n.. m:
            r.. 0

        # `dp[w]` means the maximum value
        # with weight `w`
        dp = [0] * (m + 1)

        _val = 0
        ___ i __ r..(l..(A)):
            ___ w __ r..(A[i], m + 1):
                _val = dp[w - A[i]] + V[i]
                __ _val > dp[w]:
                    dp[w] = _val

        r.. dp[m]


"""
Origin
"""
c_ Solution:
    """
    @param: A: an integer array
    @param: V: an integer array
    @param: m: an integer
    @return: an integer
    """
    ___ backPackIII  A, V, m):
        __ n.. A o. n.. V o. n.. m:
            r.. 0

        n = l..(A)

        # `dp[i][w]` means the maximum value
        # with weight `w` in the former `i` items
        dp = [[0] * (m + 1) ___ _ __ r..(n + 1)]

        ___ i __ r..(1, n + 1):
            ___ w __ r..(1, m + 1):
                dp[i][w] = dp[i - 1][w]

                __ w >= A[i - 1]:
                    dp[i][w] = m..(
                        dp[i][w],
                        dp[i][w - A[i - 1]] + V[i - 1]
                    )

        r.. dp[n][w]
