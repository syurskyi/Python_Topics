#!/usr/bin/python3
"""
Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t
is potentially a very long (length ~= 500,000) string, and s is a short string
(<=100).

A subsequence of a string is a new string which is formed from the original
string by deleting some (can be none) of the characters without disturbing the
relative positions of the remaining characters. (ie, "ace" is a subsequence of
"abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"
Return true.

Example 2:
s = "axc", t = "ahbgdc"
Return false.

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you
want to check one by one to see if T has its subsequence. In this scenario, how
would you change your code?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases
"""
____ bisect _______ bisect_left
____ collections _______ defaultdict


class Solution:
    ___ isSubsequence(self, s: s.., t: s..) -> bool:
        """
        Subsequence - Binary search
        """
        char_pos = defaultdict(l..)
        ___ p, c __ e..(t):
            char_pos[c].a..(p)
            # the list is naturally sorted

        lo_po = -1
        ___ c __ s:
            __ c n.. __ char_pos:
                r.. False
            pos = char_pos[c]
            i = bisect_left(pos, lo_po)
            __ i __ l..(pos):
                r.. False
            lo_po = pos[i] + 1  # pitfall

        r.. True


__ __name__ __ "__main__":
    ... Solution().isSubsequence("abc", "ahbgdc") __ True
    ... Solution().isSubsequence("acb", "ahbgdc") __ False
