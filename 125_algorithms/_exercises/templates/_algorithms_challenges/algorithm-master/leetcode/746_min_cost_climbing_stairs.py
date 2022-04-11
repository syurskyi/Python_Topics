c_ Solution:
    ___ minCostClimbingStairs  cost
        """
        :type cost: List[int]
        :rtype: int
        """

        __ n.. cost:
            r.. 0

        n l..(cost)

        """
        `dp[i]` means the min cost to possible to reach previous `i` steps
        """
        dp [0] * (n + 1)

        ___ i __ r..(2, n + 1
            """
            If you decide to come from some step,
            and then pay the fee to the from step
            """
            dp[i] m..(
                dp[i - 1] + cost[i - 1],
                dp[i - 2] + cost[i - 2]
            )

        r.. dp[n]
