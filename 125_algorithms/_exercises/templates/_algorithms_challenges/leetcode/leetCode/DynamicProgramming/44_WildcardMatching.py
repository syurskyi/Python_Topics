#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ isMatch  s, p
        """ Dynamic Programming

        dp[i][j] represents isMatch(p[0...i-1], s[0...j-1]), default is False;
        dp[i][0]: isMatch(p[0...i], ""), dp[0][j]: isMatch("", s[0...j])
        dp[0][0] represents

        If p[i] is "*", dp[i+1][j+1] =
            1. dp[i][j+1]        # * matches 0 element in s;
            2. dp[i][j]          # * matches 1 element in s;
            3. dp[i+1][j]        # * matches more than one in s.
        """
        __ n.. s:
            __ p.c..('*') != l..(p
                r_ False
            r_ True

        # Optimized for the big data.
        __ l..(p) - p.c..('*') > l..(s
            r_ False

        # Initinal process
        dp = [[False ___ col __ r..(l..(s) + 1)] ___ row __ r..(l..(p) + 1)]
        dp[0][0] = True     # isMatch("", "") = True
        ___ i __ r..(l..(p)):
            dp[i + 1][0] = dp[i][0] a.. p[i] __ '*'

        ___ i __ r..(l..(p)):
            ___ j __ r..(l..(s)):
                __ p[i] __ "*":
                    dp[i + 1][j + 1] = dp[i][j + 1] or dp[i][j] or dp[i + 1][j]
                ____
                    dp[i + 1][j + 1] = dp[i][j] a.. (p[i] __ s[j] or p[i] __ "?")

        r_ dp[l..(p)][l..(s)]

"""
"aa"
"a"
"aa"
"aa"
"aaa"
"aa"
"aa"
"*"
"aa"
"a*"
"ab"
"?*"
"aab"
"c*a*b"
"""
