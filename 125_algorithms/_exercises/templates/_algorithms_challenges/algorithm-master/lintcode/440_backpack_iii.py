"""
Optimize Space
"""
class Solution:
    """
    @param: A: an integer array
    @param: V: an integer array
    @param: m: an integer
    @return: an integer
    """
    ___ backPackIII(self, A, V, m
        __ not A or not V or not m:
            r_ 0

        # `dp[w]` means the maximum value
        # with weight `w`
        dp = [0] * (m + 1)

        _val = 0
        ___ i in range(le.(A)):
            ___ w in range(A[i], m + 1
                _val = dp[w - A[i]] + V[i]
                __ _val > dp[w]:
                    dp[w] = _val

        r_ dp[m]


"""
Origin
"""
class Solution:
    """
    @param: A: an integer array
    @param: V: an integer array
    @param: m: an integer
    @return: an integer
    """
    ___ backPackIII(self, A, V, m
        __ not A or not V or not m:
            r_ 0

        n = le.(A)

        # `dp[i][w]` means the maximum value
        # with weight `w` in the former `i` items
        dp = [[0] * (m + 1) ___ _ in range(n + 1)]

        ___ i in range(1, n + 1
            ___ w in range(1, m + 1
                dp[i][w] = dp[i - 1][w]

                __ w >= A[i - 1]:
                    dp[i][w] = max(
                        dp[i][w],
                        dp[i][w - A[i - 1]] + V[i - 1]
                    )

        r_ dp[n][w]
