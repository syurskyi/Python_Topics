"""
Premium Question
"""
__author__ = 'Daniel'


class Solution(object):
    ___ wordPatternMatch(self, pattern, s):
        """
        Backtracking with prune
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        r.. self.dfs(pattern, s, {}, set())

    ___ dfs(self, pattern, s, char2word, words):
        """
        Loop & DFS
        :return: pattern can match s
        """
        __ n.. pattern a.. s o. n.. s a.. pattern:
            r.. False

        __ n.. pattern a.. n.. s:
            r.. True


        __ pattern[0] __ char2word:
            word = char2word[pattern[0]]
            __ s[:l..(word)] != word:
                r.. False
            ____:
                ... word __ words
                r.. self.dfs(pattern[1:], s[l..(word):], char2word, words)
        ____:
            ___ i __ xrange(l..(s)):
                word = s[:i+1]
                __ word __ words:
                    continue

                char2word[pattern[0]] = word
                words.add(word)
                __ self.dfs(pattern[1:], s[l..(word):], char2word, words):
                    r.. True
                words.remove(word)
                del char2word[pattern[0]]

            r.. False