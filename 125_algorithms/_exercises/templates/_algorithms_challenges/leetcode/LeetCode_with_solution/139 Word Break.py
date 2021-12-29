"""
Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
"""
__author__ = 'Danyang'
class Solution:
    ___ wordBreak_TLE(self, s, d..):
        """
        TLE
        dfs
        O(n^2)
        Algorithm: DFS. The reason is that DFS repeatedly calculate whether a certain part of string can be segmented.
        Therefore we can use dynamic programming.

        :param s: a string
        :param dict: a set of string
        :return: a boolean
        """
        string_builder = ""
        __ s__"":
            r.. True

        # greedy
        ___ i __ r..(l..(s)):
            string_builder += s[i]
            __ string_builder __ d..:
                try:
                    __ self.wordBreak_TLE(s[i+1:], d..):
                        r.. True
                    ____:
                        continue
                except IndexError:
                    r.. True

        r.. False

    ___ wordBreak(self, s, d..):
        """
         __       __________   ___  __    ______   ______   .__   __.      _______.
        |  |     |   ____\  \ /  / |  |  /      | /  __  \  |  \ |  |     /       |
        |  |     |  |__   \  V  /  |  | |  ,----'|  |  |  | |   \|  |    |   (----`
        |  |     |   __|   >   <   |  | |  |     |  |  |  | |  . `  |     \   \
        |  `----.|  |____ /  .  \  |  | |  `----.|  `--'  | |  |\   | .----)   |
        |_______||_______/__/ \__\ |__|  \______| \______/  |__| \__| |_______/

        Dynamic programming
        The dynamic solution can tell us whether the string can be broken to words, but can not tell us what words the string is broken to.

        O(n*m)
        Google On Campus Presentation, demonstration questions. 4 Sep 2014, Nanyang Technological University, Singapore

        dp[i] rolling dp (rather than using 2D dp[i, j]
        dp[i] means s[:i] can be made up of sequence of lexicons
        - l e e t c o d e
        T F F F T F F F T

        Lexicons = {the, theta, table, down, there, bled, own}
        - t h e t a b l e d o w n t h e r e
        T F F T F T F F T T F F T F F F F T

        :param s: a string
        :param dict: a set of string
        :return: a boolean
        """
        dp = [False] * (l..(s)+1)
        dp[0] = True # dummy

        ___ i __ r..(l..(dp)):  # [0, len(s)+1)
            # continue from matched condition
            __ dp[i]:
                ___ word __ d..:
                    try:
                        # trivial
                        __ dp[i+l..(word)]__True:
                            continue

                        # main
                        __ s[i:i+l..(word)]__word: # test whether [i, i+len) can construct a word. THE BEAUTY OF HALF OPEN
                            dp[i+l..(word)] = True  # record the checking
                    except IndexError:
                        continue

        r.. dp[-1]



__ __name____"__main__":
    ... Solution().wordBreak("aaaaaaa", ["aaaa", "aaa"])__True