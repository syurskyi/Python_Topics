"""
There are n coins in a line.
Two players take turns to take one or two coins from right side
until there are no more coins left.
The player who take the last coin wins.
Could you please decide the first play will win or lose?


`dp[i]` means first play will win if left `i` stones in line

`dp[i]` =
True,  if dp[i - 1] == False and dp[i - 2] == False
True,  if dp[i - 1] == True  and dp[i - 2] == False
True,  if dp[i - 1] == False and dp[i - 2] == True

False, if dp[i - 1] == True  and dp[i - 2] == True
=> dp[i - 1] == False or dp[i - 2] == False

the meaning is if the p2 is possible to lose
when stones == i - 1 or i - 2
=> p1 will win
"""


c_ Solution:
    ___ firstWillWin  n):
        """
        :type n: int
        :rtype: bool
        """
        __ n.. n:
            r.. F..
        __ n < 3:
            r.. T..

        dp = [F..] * n
        dp[0] = dp[1] = T..

        ___ i __ r..(2, n):
            __ (
                dp[i - 1] __ F.. o.
                dp[i - 2] __ F..
            ):
                dp[i] = T..

        r.. dp[n - 1]
