"""
Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") -> false
isMatch("aa","aa") -> true
isMatch("aaa","aa") -> false
isMatch("aa", "*") -> true
isMatch("aa", "a*") -> true
isMatch("ab", "?*") -> true
isMatch("aab", "c*a*b") -> false
"""
__author__ = 'Danyang'
class Solution:
    ___ isMatch_MLE(self, s, p
        """
        dp, similar to 011 Regular Expression Matching.
        Backward dp

        but Memory Limit Exceeds

        :param s: tape, an input string
        :param p: pattern, a pattern string
        :return: boolean
        """
        tape = s
        pattern = p

        m = le.(tape)
        n = le.(pattern)
        dp = [[False for _ in xrange(n+1)] for _ in xrange(m+1)]
        # edge cases
        dp[m][n] = True
        for j in xrange(n-1, -1 , -1
            __ pattern[j]__"*":
                dp[m][j] = dp[m][j+1]

        # transition
        for i in xrange(m-1, -1, -1
            for j in xrange(n-1, -1, -1
                __ tape[i]__pattern[j] or pattern[j]__"?":
                    dp[i][j] = dp[i+1][j+1]
                ____ pattern[j]__"*":
                    dp[i][j] = dp[i][j+1] or dp[i+1][j]  # zero or more
                ____
                    dp[i][j] = False


        r_ dp[0][0]

    ___ isMatch_forward(self, s, p
        """
        "?" is not the problem
        "*" is the problem
        Forward dp:
        dp starting from -1
        if pattern[j]!="*", dp[i][j] = dp[i-1][j-1] && tape[i] matches pattern[j]
        if pattern[j]=="*", dp[i][j] = any(dp[m][j-1])  w.r.t m

        Compact the 2-D dp to 1-D dp:
        iterate through j, since we only need know j-1 state, thus dropping the dimension for j in dp

        :param s: tape, an input string
        :param p: pattern, a pattern string
        :return: boolean
        """
        tape = s
        pattern = p

        m = le.(tape)
        n = le.(pattern)

        __ n - list(pattern).count("*") > m:
            r_ False

        dp = [False for _ in xrange(m+1)]
        dp[0] = True  # dummy
        for j in xrange(1, n+1
            __ pattern[j-1]__"*":
                # for i in xrange(m, 0, -1
                #     dp[i] = any(dp[k] for k in xrange(i))  # Time Complexity
                k = 0
                w___ k<m+1 and dp[k]!=True: k+= 1
                for i in xrange(k, m+1
                    dp[i] = True
            ____
                for i in xrange(m, 0, -1
                    dp[i] = dp[i-1] and (tape[i-1]__pattern[j-1] or pattern[j-1]__"?")

            dp[0] = dp[0] and pattern[j-1]__"*"  # !!, pattern no longer match the empty string


        r_ dp[m]

__ __name____"__main__":
    assert Solution().isMatch("aab", "c*a*b")__False
    assert Solution().isMatch("aa","a")__False
    assert Solution().isMatch("aa", "aa")__True
    assert Solution().isMatch("aaa", "aa")__False
    assert Solution().isMatch("aaa", "*")__True
    assert Solution().isMatch("aa", "a*")__True
    assert Solution().isMatch("ab", "?*")__True
