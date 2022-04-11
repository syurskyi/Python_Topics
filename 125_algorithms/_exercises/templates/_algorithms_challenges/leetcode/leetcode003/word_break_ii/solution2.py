"""
Given a string s and a dictionary of words dict, add spaces in s to construct
a sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
"""

c_ Solution(o..
    ___ wordBreak  s, wordDict
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        n l..(s)
        t [N.. ___ i __ r..(n)]
        res word_break_aux(s, wordDict, n - 1, t)
        r.. res

    ___ word_break_aux  s, wordDict, i, t
        """
        Determine if s[:i + 1] can be segmented by dict wordDict
        """
        __ s[:i + 1] __ wordDict:
            t[i] [s[:i + 1]]
            r.. t[i]
        ____ t[i] __ n.. N..
            r.. t[i]
        ____
            res    # list
            ___ j __ r..(i
                rest word_break_aux(s, wordDict, j, t)
                word s[j + 1:i + 1]
                __ rest a.. word __ wordDict:
                    ___ r __ rest:
                        res.a..(r + ' ' + word)
            t[i] res
            r.. t[i]


s1 "catsanddog"
d1 ["cat", "cats", "and", "sand", "dog"]
s Solution()
print(s.wordBreak(s1, d1
print(s.wordBreak('leetcode',  'leet', 'code'
