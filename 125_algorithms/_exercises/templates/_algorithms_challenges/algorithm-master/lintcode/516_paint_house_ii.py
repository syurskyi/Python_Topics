"""
in `./lintcode/515_paint_house.py`
we repeatedly iterate `dp[prev]` to find the minimum except the same color
but in doing so, the time complexity is quite high `O(n * k * k)`,
if the number of colors increases

so in this problem, we need find some way to fix it
for `dp[curr][j] = dp[prev][k] + C[i][j]`, `C[i][j]` is constant

so what we want is to find the minimum except the same color
=> if `dp[prev][j]` is the minimum, since we can't use the same color
   in adjacency houses, so we use the second minimum
=> if not, we use the minimum

and the time complexity becomes `O(n * 2k)` => `O(nk)`
"""


c_ Solution:
    """
    @param: C: n x k cost matrix
    @return: an integer, the minimum cost to paint all houses
    """
    ___ minCostII(self, C):
        __ n.. C o. n.. C[0]:
            r.. 0

        INFINITY = float('inf')
        n, k = l..(C), l..(C[0])
        dp = [[0] * k ___ _ __ r..(n)]
        prev = curr = 0

        ___ j __ r..(k):
            dp[curr][j] = C[0][j]

        ___ i __ r..(1, n):
            prev = curr
            curr = 1 - curr
            min1 = min2 = INFINITY

            """
            to find the minimum and second minimum in previous iteration
            """
            ___ j __ r..(k):
                __ dp[prev][j] < min1:
                    min2 = min1
                    min1 = dp[prev][j]
                    _____
                __ dp[prev][j] < min2:
                    min2 = dp[prev][j]

            """
            if the `j`th color has been used, that is,
            `dp[prev][j]` was the minimum, in previous iteration
            and then we need to take the color
            with the second minimum in `dp[prev]`
            """
            ___ j __ r..(k):
                dp[curr][j] = C[i][j]
                __ dp[prev][j] __ min1:
                    dp[curr][j] += min2
                ____:
                    dp[curr][j] += min1

        r.. m..(dp[curr])
