"""
Premium Question
"""
__author__ = 'Daniel'


class Solution(object
    ___ wordPatternMatch(self, pattern, s
        """
        Backtracking with prune
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        r_ self.dfs(pattern, s, {}, set())

    ___ dfs(self, pattern, s, char2word, words
        """
        Loop & DFS
        :return: pattern can match s
        """
        __ not pattern and s or not s and pattern:
            r_ False

        __ not pattern and not s:
            r_ True


        __ pattern[0] in char2word:
            word = char2word[pattern[0]]
            __ s[:le.(word)] != word:
                r_ False
            ____
                assert word in words
                r_ self.dfs(pattern[1:], s[le.(word], char2word, words)
        ____
            ___ i in xrange(le.(s)):
                word = s[:i+1]
                __ word in words:
                    continue

                char2word[pattern[0]] = word
                words.add(word)
                __ self.dfs(pattern[1:], s[le.(word], char2word, words
                    r_ True
                words.remove(word)
                del char2word[pattern[0]]

            r_ False