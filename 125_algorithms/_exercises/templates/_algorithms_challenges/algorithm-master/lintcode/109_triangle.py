"""
DP: Memory Searching
"""
c_ Solution:
    """
    @param: triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    ___ minimumTotal  triangle
        __ n.. triangle o. n.. triangle[0]:
            r.. 0

        r.. memo_search(0, 0, triangle, {})

    ___ memo_search  depth, start, triangle, memo
        __ depth __ l..(triangle) - 1:
            r.. triangle[depth][start]

        key = (depth, start)

        __ key __ memo:
            r.. memo[key]

        memo[key] = m..(
            memo_search(depth + 1, start, triangle, memo),
            memo_search(depth + 1, start + 1, triangle, memo)
        )

        memo[key] += triangle[depth][start]

        r.. memo[key]


"""
DP: Top-down Recuring + Rolling Array
"""
c_ Solution:
    """
    @param: triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    ___ minimumTotal  triangle
        __ n.. triangle o. n.. triangle[0]:
            r.. 0

        INFINITY = f__('inf')
        m = l..(triangle)
        dp = [[INFINITY] * (m + 1) ___ _ __ r..(2)]

        prev = curr = 0
        ___ i __ r..(1, m + 1
            prev = curr
            curr = 1 - curr

            ___ j __ r..(1, i + 1
                """
                dp[prev][j] == dp[i - 1][j]
                dp[curr][j] == dp[i][j]
                """

                dp[curr][j] = triangle[i - 1][j - 1]

                __ dp[prev][j - 1] < INFINITY o. dp[prev][j] < INFINITY:
                    """
                    NO need to calculate first,
                    since only one path from top
                    """
                    dp[curr][j] += m..(
                        dp[prev][j - 1],
                        dp[prev][j]
                    )

        r.. m..(dp[curr])


"""
DP: Bottom-up Recuring + Rolling Array
"""
c_ Solution:
    """
    @param: triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    ___ minimumTotal  triangle
        __ n.. triangle o. n.. triangle[0]:
            r.. 0

        INFINITY = f__('inf')
        m = l..(triangle)
        dp = [[INFINITY] * (m + 1) ___ _ __ r..(m + 1)]

        prev = curr = 0
        ___ i __ r..(m - 1, -1, -1
            prev = curr
            curr = 1 - curr

            ___ j __ r..(i + 1
                """
                dp[prev][j] == dp[i + 1][j]
                dp[curr][j] == dp[i][j]
                """

                dp[curr][j] = triangle[i][j]

                __ dp[prev][j] < INFINITY o. dp[prev][j + 1] < INFINITY:
                    """
                    MUST be calculated first,
                    since there are two paths from bottom
                    and `dp[curr][j]` maybe negative
                    """
                    dp[curr][j] = m..(
                        dp[curr][j] + dp[prev][j],
                        dp[curr][j] + dp[prev][j + 1]
                    )

        r.. dp[curr][0]
