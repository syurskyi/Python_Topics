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
        n = l..(s)
        t = [N.. ___ i __ r..(n)]
        r.. word_break_aux(s, wordDict, n - 1, t)

    ___ word_break_aux  s, wordDict, i, t
        """
        Determine if s[:i + 1] can be segmented by dict wordDict
        """
        __ s[:i + 1] __ wordDict:
            r.. T..
        ____ t[i] __ n.. N..
            r.. t[i]
        ____:
            ___ j __ r..(i
                __ (word_break_aux(s, wordDict, j, t) __ T..
                        a.. s[j + 1:i + 1] __ wordDict
                    t[i] = T..
                    r.. T..
            ____:
                t[i] = F..
                r.. F..


s = Solution()
print(s.wordBreak('leetcode',  'leet', 'code'
print(s.wordBreak('leetcode',  'lee', 'code'
