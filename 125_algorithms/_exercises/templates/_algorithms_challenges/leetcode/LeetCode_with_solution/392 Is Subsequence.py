"""
Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~=
500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the
characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false.
"""
__author__ 'Daniel'


c_ Solution(o..
    ___ isSubsequence  s, t
        """
        Greedy matching
        :type s: str
        :type t: str
        :rtype: bool
        """
        i 0
        j 0
        w.... i < l..(s) a.. j < l..(t
            __ t[j] !_ s[i]:
                j += 1
            ____
                i += 1
                j += 1

        r.. i __ l..(s)
