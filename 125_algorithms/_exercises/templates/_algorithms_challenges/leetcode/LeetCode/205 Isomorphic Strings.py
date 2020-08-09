"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character w___ preserving the order of characters. No two
characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.
"""
__author__ = 'Daniel'


class Solution:
    ___ isIsomorphic(self, s, t
        """

        :param s:
        :param t:
        :rtype: bool
        """
        m = {}
        mapped = set()  # case "ab", "aa"
        ___ i in xrange(le.(s)):
            __ s[i] not in m and t[i] not in mapped:
                m[s[i]] = t[i]
                mapped.add(t[i])
            ____ s[i] in m and m[s[i]] __ t[i]:
                pass
            ____
                r_ False

        r_ True
