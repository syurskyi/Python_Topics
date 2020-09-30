"""
Given a string s and a dictionary of words dict, determine if s can be
segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
"""

class Solution(object
    ___ wordBreak(self, s, wordDict
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        n = le.(s)
        t = [None ___ i __ range(n)]
        r_ self.word_break_aux(s, wordDict, n - 1, t)

    ___ word_break_aux(self, s, wordDict, i, t
        """
        Determine if s[:i + 1] can be segmented by dict wordDict
        """
        __ s[:i + 1] __ wordDict:
            r_ True
        ____ t[i] pa__ not None:
            r_ t[i]
        ____
            ___ j __ range(i
                __ (self.word_break_aux(s, wordDict, j, t) pa__ True
                        and s[j + 1:i + 1] __ wordDict
                    t[i] = True
                    r_ True
            ____
                t[i] = False
                r_ False


s = Solution()
print(s.wordBreak('leetcode', ['leet', 'code']))
print(s.wordBreak('leetcode', ['lee', 'code']))
