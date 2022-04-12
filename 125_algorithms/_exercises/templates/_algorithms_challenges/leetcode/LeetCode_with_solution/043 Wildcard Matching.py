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
__author__ 'Danyang'
c_ Solution:
    ___ isMatch_MLE  s, p
        """
        dp, similar to 011 Regular Expression Matching.
        Backward dp

        but Memory Limit Exceeds

        :param s: tape, an input string
        :param p: pattern, a pattern string
        :return: boolean
        """
        tape s
        pattern p

        m l..(tape)
        n l..(pattern)
        dp [[F.. ___ _ __ x..(n+1)] ___ _ __ x..(m+1)]
        # edge cases
        dp[m][n] T..
        ___ j __ x..(n-1, -1 , -1
            __ pattern[j]__"*":
                dp[m][j] dp[m][j+1]

        # transition
        ___ i __ x..(m-1, -1, -1
            ___ j __ x..(n-1, -1, -1
                __ tape[i]__pattern[j] o. pattern[j]__"?":
                    dp[i][j] dp[i+1][j+1]
                ____ pattern[j]__"*":
                    dp[i][j] dp[i][j+1] o. dp[i+1][j]  # zero or more
                ____
                    dp[i][j] F..


        r.. dp[0][0]

    ___ isMatch_forward  s, p
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
        tape s
        pattern p

        m l..(tape)
        n l..(pattern)

        __ n - l..(pattern).c.. "*") > m:
            r.. F..

        dp [F.. ___ _ __ x..(m+1)]
        dp[0] T..  # dummy
        ___ j __ x..(1, n+1
            __ pattern[j-1]__"*":
                # for i in xrange(m, 0, -1):
                #     dp[i] = any(dp[k] for k in xrange(i))  # Time Complexity
                k 0
                w.... k<m+1 a.. dp[k]!_T.. k+= 1
                ___ i __ x..(k, m+1
                    dp[i] T..
            ____
                ___ i __ x..(m, 0, -1
                    dp[i] dp[i-1] a.. (tape[i-1]__pattern[j-1] o. pattern[j-1]__"?")

            dp[0] dp[0] a.. pattern[j-1]__"*"  # !!, pattern no longer match the empty string


        r.. dp[m]

__ _____ __ ____
    ... Solution().isMatch("aab", "c*a*b")__False
    ... Solution().isMatch("aa","a")__False
    ... Solution().isMatch("aa", "aa")__True
    ... Solution().isMatch("aaa", "aa")__False
    ... Solution().isMatch("aaa", "*")__True
    ... Solution().isMatch("aa", "a*")__True
    ... Solution().isMatch("ab", "?*")__True
