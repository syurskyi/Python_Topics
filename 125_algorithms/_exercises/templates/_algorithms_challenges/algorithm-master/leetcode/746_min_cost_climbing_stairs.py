class Solution:
    ___ minCostClimbingStairs(self, cost
        """
        :type cost: List[int]
        :rtype: int
        """

        __ not cost:
            r_ 0

        n = le.(cost)

        """
        `dp[i]` means the min cost to possible to reach previous `i` steps
        """
        dp = [0] * (n + 1)

        ___ i in range(2, n + 1
            """
            If you decide to come from some step,
            and then pay the fee to the from step
            """
            dp[i] = min(
                dp[i - 1] + cost[i - 1],
                dp[i - 2] + cost[i - 2]
            )

        r_ dp[n]
