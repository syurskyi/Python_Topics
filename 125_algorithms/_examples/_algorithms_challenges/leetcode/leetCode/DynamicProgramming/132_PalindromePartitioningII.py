#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    """
    Dynamic Programming:
    cuts[i]: minimum cuts needed for a palindrome partitioning of s[i:], so we want cuts[0].

    To get cuts[i-1], we scan j from i-1 to len(s)-1.
    Once we comes to a is_palindrome[i-1][j]==true:
        if j==len(s)-1, the string s[i-1:] is a Pal, cuts[i-1] is 0;
        else: the current cut num (first cut s[i-1:j+1] and then cut the rest
        s[j+1:]) is 1+cuts[j+1], compare it to the exisiting cuts[i-1], repalce if smaller.

    is_palindrome[i][j]: whether s[i:j+1] is palindrome.
    Here we need not to compute the is_palindrome in advance.
    We use "Dynamic Programming" too, the formula is very intuitive:
    is_palindrome[i][j] = true if (is_palindrome[i+1][j-1] and s[i] == s[j]) else false

    A better O(n) space solution can be found here:
    https://discuss.leetcode.com/topic/2840/my-solution-does-not-need-a-table-for-palindrome-is-it-right-it-uses-only-o-n-space
    """

    def minCut(self, s):
        if not s:
            return 0
        s_len = len(s)

        is_palindrome = [[False for i in range(s_len)]
                         for j in range(s_len)]

        cuts = [s_len - 1 - i for i in range(s_len)]
        for i in range(s_len - 1, -1, -1):
            for j in range(i, s_len):
                # if self.is_palindrome(i, j):
                if ((j - i < 2 and s[i] == s[j]) or (s[i] == s[j] and is_palindrome[i + 1][j - 1])):
                    is_palindrome[i][j] = True
                    if j == s_len - 1:
                        cuts[i] = 0
                    else:
                        cuts[i] = min(cuts[i], 1 + cuts[j + 1])
                else:
                    pass

        return cuts[0]


"""
""
"aab"
"aabb"
"aabaa"
"acbca"
"acbbca"
"""
