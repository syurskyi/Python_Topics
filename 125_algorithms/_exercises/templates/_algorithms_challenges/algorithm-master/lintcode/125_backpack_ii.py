"""
Rolling Array
"""
c_ Solution:
    """
    @param: m: An integer m denotes the size of a backpack
    @param: A: Given n items with size A[i]
    @param: V: Given n items with value V[i]
    @return: The maximum value
    """
    ___ backPackII(self, m, A, V):
        __ n.. m o. n.. A o. n.. V:
            r.. 0

        # `dp[i][w]` means the maximum value
        # with weight `w` in the former `i` items
        dp = [[0] * (m + 1) ___ _ __ r..(2)]

        prev = curr = 0
        ___ i __ r..(1, l..(A) + 1):
            prev = curr
            curr = 1 - curr
            ___ w __ r..(1, m + 1):
                dp[curr][w] = dp[prev][w]

                __ w >= A[i - 1]:
                    dp[curr][w] = max(
                        dp[curr][w],
                        dp[prev][w - A[i - 1]] + V[i - 1]
                    )

        r.. dp[curr][m]


"""
Origin
"""
c_ Solution:
    """
    @param: m: An integer m denotes the size of a backpack
    @param: A: Given n items with size A[i]
    @param: V: Given n items with value V[i]
    @return: The maximum value
    """
    ___ backPackII(self, m, A, V):
        __ n.. m o. n.. A o. n.. V:
            r.. 0

        n = l..(A)
        dp = [[0] * (m + 1) ___ _ __ r..(n + 1)]

        ___ i __ r..(1, n + 1):
            ___ w __ r..(1, m + 1):
                dp[i][w] = dp[i - 1][w]

                __ w >= A[i - 1]:
                    dp[i][w] = max(
                        dp[i][w],
                        dp[i - 1][w - A[i - 1]] + V[i - 1]
                    )

        r.. dp[n][m]
