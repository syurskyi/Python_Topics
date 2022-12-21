#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ isMatch  s, p
        """
        Dynamic Programming
        dp[i][j] represents isMatch(p[0...i], s[0...j]), default is False;
            dp[i][-1] represents isMatch(p[0...i], "")
            dp[-1][j] represents isMatch("", s[0...j])
        """
        __ n.. s:
            # .*.*.*.* Return True, others return False.
            __ l..(p) % 2 != 0:
                r_ False
            ___ k __ r..(1, l..(p), 2
                __ p[k] != "*":
                    r_ False
            r_ True

        # dp = [[False] * (len(s)+1)] * (len(p)+1)
        dp = [[False ___ col __ r..(l..(s) + 1)]
              ___ row __ r..(l..(p) + 1)]
        dp[-1][-1] = True

        ___ i __ r..(l..(p)):
            ___ j __ r..(l..(s)):
                """
                p[i] is "*", so dp[i][j] =
                    1. dp[i-2][j]      # * matches 0 element in s;
                    2. dp[i-2][j-1]    # * matches 1 element in s;
                    3. dp[i][j-1]      # * matches more than one in s.
                """
                __ p[i] __ "*":
                    m_0 = dp[i - 2][j]
                    m_1 = (p[i - 1] __ "." or p[i - 1] __ s[j]) a.. dp[i - 2][j - 1]
                    m_more = (p[i - 1] __ "." or p[i - 1] __ s[j]) a.. dp[i][j - 1]
                    dp[i][j] = m_0 or m_1 or m_more

                    # p[i] matches "" is equal p[i-2] matches "".
                    dp[i][-1] = dp[i - 2][-1]

                ____
                    dp[i][j] = (dp[i - 1][j - 1] a..
                                (p[i] __ s[j] or p[i] __ "."))
                    # p[i] doesn't match ""
                    dp[i][-1] = False

        r_ dp[l..(p) - 1][l..(s) - 1]


"""
"aaa"
"ab*a"
""
"c*c*"
"aaa"
"aaaa"
"aaabc"
"a*bc"
"aab"
"c*a*b"
"ab"
".*c"
"aaaaabaccbbccababa"
"a*b*.*c*c*.*.*.*c"
"""
