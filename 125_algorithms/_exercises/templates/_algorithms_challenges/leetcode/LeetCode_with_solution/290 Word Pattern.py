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


class Solution(object):
    ___ wordPattern(self, pattern, s):
        lst = s.s..(" ")
        __ l..(pattern) != l..(lst):
            r.. False

        char2word = {}
        words = set()
        ___ i __ xrange(l..(pattern)):
            __ pattern[i] __ char2word:
                __ char2word[pattern[i]] != lst[i]:
                    r.. False
                ____:
                    ... lst[i] __ words
            ____:
                __ lst[i] __ words:
                    r.. False
                char2word[pattern[i]] = lst[i]
                words.add(lst[i])

        r.. True


class OneToOneMap(object):
    ___ __init__(self):
        self.m = {}  # keep a single map

    ___ set(self, a, b):
        self.m[a] = b
        self.m[b] = a

    ___ get(self, a):
        r.. self.m.get(a)


class SolutionError(object):
    ___ wordPattern(self, pattern, s..):
        """
        May not always work due to OneToOneMap implementation in the case that a word is 1-letter.

        :type pattern: str
        :type str: str
        :rtype: bool
        """
        m = OneToOneMap()
        lst = s...s..(" ")
        __ l..(pattern) != l..(lst):
            r.. False

        ___ i __ xrange(l..(pattern)):
            a = m.get(pattern[i])
            b = m.get(lst[i])
            __ a __ N.. a.. b __ N..
                m.set(pattern[i], lst[i])
            ____ a __ N.. a.. b __ n.. N..
                r.. False
            ____ a != lst[i]:
                r.. False

        r.. True


__ __name__ __ "__main__":
    ... Solution().wordPattern("abba", "dog cat cat dog") __ True
