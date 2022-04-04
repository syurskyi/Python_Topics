"""
There are n coins in a line.
Two players take turns to take a coin from one of the ends of the line
until there are no more coins left.
The player with the larger amount of money wins.
Could you please decide the first player will win or lose?


`dp[i][j]` means the maximum value when
the current player chosen from [i, j] in `values`

recurring from the end of the game to start
so init with `dp[i][i]`

i   i+1     j-1  j
c1  c2  c3  c4  c5

there are two cases:
    1. if the current player chosen `values[i]`, then
       the cost is `dp[i + 1][j]`
    2. if the current player chosen `values[j]`, then
       the cost is `dp[i][j - 1]`

chosen the maximum
"""


c_ Solution:
    ___ firstWillWin  values
        """
        :type values: list[int]
        :rtype: bool
        """
        __ n.. values:
            r.. F..

        n = l..(values)

        __ n < 2:
            r.. T..

        dp = [[0] * n ___ _ __ r..(n)]

        ___ i __ r..(n
            dp[i][i] = values[i]

        ___ i __ r..(n - 1 - 1, -1, -1
            ___ j __ r..(i + 1, n
                dp[i][j] = m..((
                    values[i] - dp[i + 1][j],
                    values[j] - dp[i][j - 1],


        r.. dp[0][n - 1] >= 0
