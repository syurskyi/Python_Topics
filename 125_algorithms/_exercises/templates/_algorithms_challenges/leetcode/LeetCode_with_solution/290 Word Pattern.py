"""
Given a pattern and a string str, find if str follows the same pattern.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
patterncontains only lowercase alphabetical letters, and str contains words separated by a single space. Each word in
str contains only lowercase alphabetical letters.
Both pattern and str do not have leading or trailing spaces.
Each letter in pattern must map to a word with length that is at least 1.
"""
__author__ = 'Daniel'


c_ Solution(o..
    ___ wordPattern  pattern, s
        lst = s.s..(" ")
        __ l..(pattern) != l..(lst
            r.. F..

        char2word    # dict
        words = s..()
        ___ i __ x..(l..(pattern:
            __ pattern[i] __ char2word:
                __ char2word[pattern[i]] != lst[i]:
                    r.. F..
                ____:
                    ... lst[i] __ words
            ____:
                __ lst[i] __ words:
                    r.. F..
                char2word[pattern[i]] = lst[i]
                words.add(lst[i])

        r.. T..


c_ OneToOneMap(o..
    ___ -
        m    # dict  # keep a single map

    ___ s..  a, b
        m[a] = b
        m[b] = a

    ___ get  a
        r.. m.g.. a)


c_ SolutionError(o..
    ___ wordPattern  pattern, s..
        """
        May not always work due to OneToOneMap implementation in the case that a word is 1-letter.

        :type pattern: str
        :type str: str
        :rtype: bool
        """
        m = OneToOneMap()
        lst = s...s..(" ")
        __ l..(pattern) != l..(lst
            r.. F..

        ___ i __ x..(l..(pattern:
            a = m.g.. pattern[i])
            b = m.g.. lst[i])
            __ a __ N.. a.. b __ N..
                m.s..(pattern[i], lst[i])
            ____ a __ N.. a.. b __ n.. N..
                r.. F..
            ____ a != lst[i]:
                r.. F..

        r.. T..


__ _______ __ _______
    ... Solution().wordPattern("abba", "dog cat cat dog") __ T..
