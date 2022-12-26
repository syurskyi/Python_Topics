#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ isInterleave  s1, s2, s3
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        __ n.. s1:
            __ s2 __ s3:
                r_ True
            ____
                r_ F..
        s1_l = l..(s1)
        s2_l = l..(s2)
        s3_l = l..(s3)
        __ s3_l != s1_l + s2_l:
            r_ F..

        # dp[i][j] is true when s3[i+j-1] is formed by the interleaving of
        # s1[:i](previous i chars of s1) and s2[:j](previous j chars of s2).
        dp = [[F.. ___ j __ xrange(s2_l+1)] ___ i __ xrange(s1_l+1)]
        dp[0][0] = True

        ___ i __ xrange(1, s1_l+1
            __ s1[i-1] __ s3[i-1]:
                dp[i][0] = True
            ____
                ______

        ___ j __ xrange(1, s2_l+1
            __ s2[j-1] __ s3[j-1]:
                dp[0][j] = True
            ____
                ______

        ___ i __ xrange(1, s1_l+1
            ___ j __ xrange(1, s2_l+1
                __ (s1[i-1] __ s3[i+j-1] a.. dp[i-1][j] or
                        s2[j-1] __ s3[i+j-1] a.. dp[i][j-1]
                    dp[i][j] = True

        r_ dp[s1_l][s2_l]

"""
""
"a"
"a"
"aa"
"ab"
"abaa"
"aabcc"
"dbbca"
"aadbbbaccc"
"aaaabbbb"
"ddaacccc"
"addaacaaabbbcccb"
"""
