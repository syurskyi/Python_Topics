"""
DP: Memory Searching
"""
class Solution:
    """
    @param: triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    ___ minimumTotal(self, triangle
        __ not triangle or not triangle[0]:
            r_ 0

        r_ self.memo_search(0, 0, triangle, {})

    ___ memo_search(self, depth, start, triangle, memo
        __ depth __ le.(triangle) - 1:
            r_ triangle[depth][start]

        key = (depth, start)

        __ key __ memo:
            r_ memo[key]

        memo[key] = min(
            self.memo_search(depth + 1, start, triangle, memo),
            self.memo_search(depth + 1, start + 1, triangle, memo)
        )

        memo[key] += triangle[depth][start]

        r_ memo[key]


"""
DP: Top-down Recuring + Rolling Array
"""
class Solution:
    """
    @param: triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    ___ minimumTotal(self, triangle
        __ not triangle or not triangle[0]:
            r_ 0

        INFINITY = float('inf')
        m = le.(triangle)
        dp = [[INFINITY] * (m + 1) ___ _ __ range(2)]

        prev = curr = 0
        ___ i __ range(1, m + 1
            prev = curr
            curr = 1 - curr

            ___ j __ range(1, i + 1
                """
                dp[prev][j] == dp[i - 1][j]
                dp[curr][j] == dp[i][j]
                """

                dp[curr][j] = triangle[i - 1][j - 1]

                __ dp[prev][j - 1] < INFINITY or dp[prev][j] < INFINITY:
                    """
                    NO need to calculate first,
                    since only one path from top
                    """
                    dp[curr][j] += min(
                        dp[prev][j - 1],
                        dp[prev][j]
                    )

        r_ min(dp[curr])


"""
DP: Bottom-up Recuring + Rolling Array
"""
class Solution:
    """
    @param: triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    ___ minimumTotal(self, triangle
        __ not triangle or not triangle[0]:
            r_ 0

        INFINITY = float('inf')
        m = le.(triangle)
        dp = [[INFINITY] * (m + 1) ___ _ __ range(m + 1)]

        prev = curr = 0
        ___ i __ range(m - 1, -1, -1
            prev = curr
            curr = 1 - curr

            ___ j __ range(i + 1
                """
                dp[prev][j] == dp[i + 1][j]
                dp[curr][j] == dp[i][j]
                """

                dp[curr][j] = triangle[i][j]

                __ dp[prev][j] < INFINITY or dp[prev][j + 1] < INFINITY:
                    """
                    MUST be calculated first,
                    since there are two paths from bottom
                    and `dp[curr][j]` maybe negative
                    """
                    dp[curr][j] = min(
                        dp[curr][j] + dp[prev][j],
                        dp[curr][j] + dp[prev][j + 1]
                    )

        r_ dp[curr][0]
