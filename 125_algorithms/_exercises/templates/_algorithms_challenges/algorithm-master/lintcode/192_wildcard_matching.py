"""
Main Concept:

case 1-1: `dp[i-1][j]` means `*` may start to matched new char
=> `i-1` in `dp[i-1][j]` means to check the `?` below
    '...a?a'
         \|
    '...xa*'

case 1-2: `dp[i][j-1]` means `*` continue to matched same char
=> `j-1` in `dp[i][j-1]` means to check the `?` below
    '...aa?'
         /
    '...xa*'

case 2: `P[j-1]` is `.` and `.` always matched `S[i-1]`
case 3: `P[j-1]` is `a` and `a` == `P[j-1]` == `S[i-1]`

=> `-1` in `dp[i-1][j-1]` means previous char
"""


c_ Solution:
    ___ isMatch  s, p):
        """
        :type s: str, target string
        :type p: str, regex
        :rtype: bool
        """
        __ s __ N.. o. p __ N..
            r.. F..
        __ s __ '' a.. p __ '':
            r.. T..

        ANY = '?'
        ANY_MULTI = '*'
        m, n = l..(s), l..(p)

        """
        `dp[i][j]` means the substr end at `S[i - 1]` was matched by
        the substr end at `P[j - 1]`
        """
        dp = [[F..] * (n + 1) ___ _ __ r..(m + 1)]
        dp[0][0] = T..
        # dp[i][0] = False
        # dp[0][j] -> need to check

        ___ i __ r..(m + 1):
            ___ j __ r..(1, n + 1):
                __ p[j - 1] __ ANY_MULTI:
                    dp[i][j] = dp[i - 1][j] o. dp[i][j - 1]
                ____ p[j - 1] __ ANY a.. dp[i - 1][j - 1]:
                    dp[i][j] = T..
                ____ p[j - 1] __ s[i - 1] a.. dp[i - 1][j - 1]:
                    dp[i][j] = T..

        r.. dp[m][n]
