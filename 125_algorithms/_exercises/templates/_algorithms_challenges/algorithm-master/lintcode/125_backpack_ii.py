"""
Rolling Array
"""
class Solution:
    """
    @param: m: An integer m denotes the size of a backpack
    @param: A: Given n items with size A[i]
    @param: V: Given n items with value V[i]
    @return: The maximum value
    """
    ___ backPackII(self, m, A, V
        __ not m or not A or not V:
            r_ 0

        # `dp[i][w]` means the maximum value
        # with weight `w` in the former `i` items
        dp = [[0] * (m + 1) ___ _ in range(2)]

        prev = curr = 0
        ___ i in range(1, le.(A) + 1
            prev = curr
            curr = 1 - curr
            ___ w in range(1, m + 1
                dp[curr][w] = dp[prev][w]

                __ w >= A[i - 1]:
                    dp[curr][w] = max(
                        dp[curr][w],
                        dp[prev][w - A[i - 1]] + V[i - 1]
                    )

        r_ dp[curr][m]


"""
Origin
"""
class Solution:
    """
    @param: m: An integer m denotes the size of a backpack
    @param: A: Given n items with size A[i]
    @param: V: Given n items with value V[i]
    @return: The maximum value
    """
    ___ backPackII(self, m, A, V
        __ not m or not A or not V:
            r_ 0

        n = le.(A)
        dp = [[0] * (m + 1) ___ _ in range(n + 1)]

        ___ i in range(1, n + 1
            ___ w in range(1, m + 1
                dp[i][w] = dp[i - 1][w]

                __ w >= A[i - 1]:
                    dp[i][w] = max(
                        dp[i][w],
                        dp[i - 1][w - A[i - 1]] + V[i - 1]
                    )

        r_ dp[n][m]
