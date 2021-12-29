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
        return self.dfs(pattern, s, {}, set())

    ___ dfs(self, pattern, s, char2word, words):
        """
        Loop & DFS
        :return: pattern can match s
        """
        __ not pattern and s or not s and pattern:
            return False

        __ not pattern and not s:
            return True


        __ pattern[0] in char2word:
            word = char2word[pattern[0]]
            __ s[:len(word)] != word:
                return False
            else:
                assert word in words
                return self.dfs(pattern[1:], s[len(word):], char2word, words)
        else:
            for i in xrange(len(s)):
                word = s[:i+1]
                __ word in words:
                    continue

                char2word[pattern[0]] = word
                words.add(word)
                __ self.dfs(pattern[1:], s[len(word):], char2word, words):
                    return True
                words.remove(word)
                del char2word[pattern[0]]

            return False