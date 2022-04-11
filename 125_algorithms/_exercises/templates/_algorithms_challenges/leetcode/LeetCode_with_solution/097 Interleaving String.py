"""
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
"""
__author__ 'Danyang'


c_ Solution(o..
    ___ isInterleave  s1, s2, s3
        """
        dfs
        dp

        dp[i][j], for s3[:i+j] interleaved by s1[:i], s2[:j]

          - d b b c a
        - T F F F F F
        a T F F F F F
        a T T T T T F
        b F T T F T F
        c F F T T T T
        c F F F T F T

        notice the boundary condition


        Thought:
        dfs, easy to come up, but high space complexity
        thus, dp
        f[i][j] represents s3[:i+j] comes from s1[:i] and s2[:j]
        two possible conditions:
        1. s[i+j] = s[i]
        2. s[i+j] = s[j]
        others are false

        f[i][j] = f[i-1][j] if s3[i+j]==s1[i]
                = f[i][j-1] if s3[i+j]==s2[j]
                = false

        :type s1: str
        :type s2: str
        :type s3: str
        :param s1:
        :param s2:
        :param s3:
        :return: boolean
        """
        m l..(s1)
        n l..(s2)
        __ m+n != l..(s3
            r.. F..

        dp [[F.. ___ _ __ x..(n+1)] ___ _ __ x..(m+1)]

        # initialize boundary conditions
        dp[0][0] T..
        ___ i __ x..(1, m+1
            dp[i][0] dp[i-1][0] a.. s3[i+0-1] __ s1[i-1]
        ___ j __ x..(1, n+1
            dp[0][j] dp[0][j-1] a.. s3[0+j-1] __ s2[j-1]

        # calculating
        ___ i __ x..(1, m+1
            ___ j __ x..(1, n+1
                __ n.. dp[i][j]:
                    dp[i][j] dp[i-1][j] a.. s3[i+j-1] __ s1[i-1]
                __ n.. dp[i][j]:
                    dp[i][j] dp[i][j-1] a.. s3[i+j-1] __ s2[j-1]

        r.. dp[-1][-1]

    ___ isInterleave_TLE  s1, s2, s3
        """
        dfs
        Time Limit Exceeded
        :param s1:
        :param s2:
        :param s3:
        :return: boolean
        """
        __ n.. s3:
            r.. T..
        letter s3[0]
        __ s1 a.. s1[0] __ letter:
            __ isInterleave(s1[1:], s2, s3[1:]
                r.. T..
        __ s2 a.. s2[0] __ letter:
            __ isInterleave(s1, s2[1:], s3[1:]
                r.. T..
        r.. F..


__ _______ __ _______
    ... Solution().isInterleave("aa", "ab", "abaa") __ T..
    ... Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac") __ T..
    ... Solution().isInterleave("aabcc", "dbbca", "aadbbbaccc") __ F..