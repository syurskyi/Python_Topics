"""
to borrow the idea of `./lintcode/515_paint_house.py`
a house can be at one of two status: steal or not
"""
c_ Solution:
    """
    @param: A: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """
    ___ houseRobber  A):
        __ n.. A:
            r.. 0

        n = l..(A)
        prev = curr = 0
        dp = [[0] * 2 ___ _ __ r..(2)]
        dp[0][1] = A[0]

        ___ i __ r..(1, n):
            prev = curr # (i - 1) % 2
            curr = i % 2

            dp[curr][0] = m..(dp[prev])
            dp[curr][1] = dp[prev][0] + A[i]

        r.. m..(dp[curr])


c_ Solution:
    """
    @param: A: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """
    ___ houseRobber  A):
        __ n.. A:
            r.. 0
        __ l..(A) __ 1:
            r.. A[0]

        n = l..(A)

        # `dp[i]`: the maximum amount of money we can get until house `i`
        dp = [0] * 3

        dp[0] = A[0]
        dp[1] = m..(A[0], A[1])

        prev2, prev1, curr = 0, 0, 1
        ___ i __ r..(2, n):
            prev2, prev1 = prev1, curr
            curr = i % 3

            """
            if house `i` was stolen, we can't steal house `i - 1`,
            the amount is `dp[i - 2] + A[i]`
            if house `i` is not stolen, we can steal house `i - 1`,
            but we lose the `A[i]`,
            the amount is `dp[i - 1] + 0`
            """
            dp[curr] = m..(dp[prev1], dp[prev2] + A[i])

        r.. dp[curr]


c_ Solution:
    ___ houseRobber  A):
        """
        :type A: List[int]
        :rtype: int
        """
        __ n.. A:
            r.. 0

        n = l..(A)
        dp = [0] * (n + 1)
        dp[1] = A[0]

        ___ i __ r..(2, n + 1):
            dp[i] = m..(
                dp[i - 2] + A[i - 1],
                dp[i - 1]
            )

        r.. dp[n]
