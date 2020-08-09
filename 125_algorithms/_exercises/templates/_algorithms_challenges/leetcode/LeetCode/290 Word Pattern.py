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


class Solution(object
    ___ wordPattern(self, pattern, s
        lst = s.split(" ")
        __ le.(pattern) != le.(lst
            r_ False

        char2word = {}
        words = set()
        ___ i in xrange(le.(pattern)):
            __ pattern[i] in char2word:
                __ char2word[pattern[i]] != lst[i]:
                    r_ False
                ____
                    assert lst[i] in words
            ____
                __ lst[i] in words:
                    r_ False
                char2word[pattern[i]] = lst[i]
                words.add(lst[i])

        r_ True


class OneToOneMap(object
    ___ __init__(self
        self.m = {}  # keep a single map

    ___ set(self, a, b
        self.m[a] = b
        self.m[b] = a

    ___ get(self, a
        r_ self.m.get(a)


class SolutionError(object
    ___ wordPattern(self, pattern, str
        """
        May not always work due to OneToOneMap implementation in the case that a word is 1-letter.

        :type pattern: str
        :type str: str
        :rtype: bool
        """
        m = OneToOneMap()
        lst = str.split(" ")
        __ le.(pattern) != le.(lst
            r_ False

        ___ i in xrange(le.(pattern)):
            a = m.get(pattern[i])
            b = m.get(lst[i])
            __ a is None and b is None:
                m.set(pattern[i], lst[i])
            ____ a is None and b is not None:
                r_ False
            ____ a != lst[i]:
                r_ False

        r_ True


__ __name__ __ "__main__":
    assert Solution().wordPattern("abba", "dog cat cat dog") __ True
