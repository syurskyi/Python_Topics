"""
Given a string s and a dictionary of words dict, add spaces in s to construct
a sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
"""

c_ Solution(object):
    ___ wordBreak  s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]

        Time Limit Exceeded
        """
        cand    # list
        res    # list
        word_break_aux(s, wordDict, cand, res)
        r.. res

    ___ word_break_aux  s, wordDict, cand, res):
        """
        Determine if s[:i + 1] can be segmented by dict wordDict
        """
        __ n.. s:
            res.a..(' '.j..(cand))
        ____:
            ___ i, c __ e..(s):
                word = s[:i + 1]
                rest = s[i + 1:]
                __ word __ wordDict:
                    cand.a..(word)
                    word_break_aux(rest, wordDict, cand, res)
                    cand.pop()


s1 = "catsanddog"
d1 = ["cat", "cats", "and", "sand", "dog"]
s = Solution()
print(s.wordBreak(s1, d1))
