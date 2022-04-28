c_ Solution o..
    ___ isMatch  s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # bottom up o(m*n)
        # https://leetcode.com/discuss/93024/easy-dp-java-solution-with-detailed-explanation
        __ s __ p:
            r_ True
        m, n = l.. s), l.. p)
        dp = [[False] * (n + 1) ___ _ __ r.. m + 1)]
        dp[0][0] = True
        ___ j __ r.. 1, n):
            __ p[j] __ '*' and dp[0][j - 1]:
                dp[0][j + 1] = True
        # print dp
        ___ i __ r.. m):
            ___ j __ r.. n):
                __ p[j] __ '.' or p[j] __ s[i]:
                    dp[i + 1][j + 1] = dp[i][j]
                ____ p[j] __ '*':
                    __ p[j - 1] != s[i] and p[j - 1] != '.':
                        dp[i + 1][j + 1] = dp[i + 1][j - 1]
                    ____
                        dp[i + 1][j + 1] = dp[i + 1][j] or dp[i][j + 1] or dp[i + 1][j - 1]
        r_ dp[m][n]


__ ____ __ ____
    # begin
    s  ?
    print s.isMatch("", ".*")


