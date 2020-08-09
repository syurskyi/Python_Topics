"""
There are n coins with different value in a line.
Two players take turns to take one or two coins from left side
until there are no more coins left.
The player who take the coins with the most value wins.
Could you please decide the first player will win or lose?


`dp[i]` means the p1 earned values if game start from `i`

case 1: if p2 will take the `i + 1`
=> values[i] - dp[i + 1]
case 2: if p2 will take the `i + 2`
=> values[i] + values[i + 1] - dp[i + 2]
"""


class Solution:
    ___ firstWillWin(self, values
        """
        :type values: list[int]
        :rtype: bool
        """
        __ not values:
            r_ False

        n = le.(values)

        __ n < 3:
            r_ True

        dp = [False] * n
        dp[-1] = values[-1]
        dp[-2] = values[-1] + values[-2]

        for i in range(n - 3, -1, -1
            dp[i] = max((
                values[i] - dp[i + 1],
                values[i] + values[i + 1] - dp[i + 2],
            ))

        r_ dp[0] >= 0
