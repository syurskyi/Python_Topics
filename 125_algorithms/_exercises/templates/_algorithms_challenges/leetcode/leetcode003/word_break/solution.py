"""
Given a string s and a dictionary of words dict, determine if s can be
segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
"""

c_ Solution(o..
    ___ wordBreak  s, wordDict
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        n l..(s)
        # t[i] indicates s[:i + 1] is such a string
        t [F.. ___ i __ r..(n)]
        ___ i __ r..(n
            __ s[:i + 1] __ wordDict:
                t[i] T..
            ____
                ___ j __ r..(i
                    __ t[j] __ T.. a.. s[j + 1:i + 1] __ wordDict:
                        t[i] T..
                        _____
        r.. t[-1]
