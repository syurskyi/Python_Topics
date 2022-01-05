"""
Main Concept:

end by '*' and has no matched
case 1-1: `P[j-2:j]` is `c*` and have no matched in `S`
=> `j-2` in `dp[i][j-2]` means ignored `c` and `*`

end by `*` and is the last matched in `*`
case 1-2: `P[j-2:j]` is `.*` and `.` always matched `S[i-1]`
case 1-3: `P[j-2:j]` is `a*` and `a` == `P[j-2]` == `S[i-1]`
=> `i-1` in `dp[i-1][j]` means to check the `?` below
    '...a?a'
         \|
    '...xa*'

case 2: `P[j-1]` is `.` and `.` always matched `S[i-1]`
case 3: `P[j-1]` is `a` and `a` == `P[j-1]` == `S[i-1]`
=> `-1` in `dp[i-1][j-1]` means previous char
"""


c_ Solution:
    ___ isMatch  s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        __ s __ p __ '':
            r.. T..

        m, n = l..(s), l..(p)
        MULTI = '*'
        ANY = '.'

        """
        `dp[i][j]` means the substr end at `s[i - 1]` was matched by
        the substr end at `p[j - 1]`
        """
        dp = [[F..] * (n + 1) ___ _ __ r..(m + 1)]
        dp[0][0] = T..
        # dp[i][0] = False  # i = 1 -> m + 1
        # dp[0][j] -> ?, need to check

        ___ i __ r..(m + 1):
            ___ j __ r..(1, n + 1):
                __ i > 0 a.. p[j - 1] __ s[i - 1] a.. dp[i - 1][j - 1]:
                    dp[i][j] = T..
                ____ i > 0 a.. p[j - 1] __ ANY a.. dp[i - 1][j - 1]:
                    dp[i][j] = T..
                ____ j > 1 a.. p[j - 1] __ MULTI:
                    __ dp[i][j - 2]:
                        dp[i][j] = T..
                    ____ i > 0 a.. p[j - 2] __ s[i - 1] a.. dp[i - 1][j]:
                        dp[i][j] = T..
                    ____ i > 0 a.. p[j - 2] __ ANY a.. dp[i - 1][j]:
                        dp[i][j] = T..

        r.. dp[m][n]
