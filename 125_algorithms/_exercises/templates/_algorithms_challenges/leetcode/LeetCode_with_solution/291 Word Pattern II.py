"""
Premium Question
"""
__author__ 'Daniel'


c_ Solution(o..
    ___ wordPatternMatch  pattern, s
        """
        Backtracking with prune
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        r.. dfs(pattern, s, {}, s..

    ___ dfs  pattern, s, char2word, words
        """
        Loop & DFS
        :return: pattern can match s
        """
        __ n.. pattern a.. s o. n.. s a.. pattern:
            r.. F..

        __ n.. pattern a.. n.. s:
            r.. T..


        __ pattern[0] __ char2word:
            word char2word[pattern[0]]
            __ s[:l.. ?] !_ word:
                r.. F..
            ____
                ... word __ words
                r.. dfs(pattern[1:], s[l..(word], char2word, words)
        ____
            ___ i __ x..(l..(s:
                word s[:i+1]
                __ word __ words:
                    _____

                char2word[pattern[0]] word
                words.add(word)
                __ dfs(pattern[1:], s[l..(word], char2word, words
                    r.. T..
                words.remove(word)
                del char2word[pattern[0]]

            r.. F..