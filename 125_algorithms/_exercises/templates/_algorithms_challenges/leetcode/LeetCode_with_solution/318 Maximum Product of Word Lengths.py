"""
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share
common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return
0.

Example 1:
Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
The two words can be "abcw", "xtfn".

Example 2:
Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Return 4
The two words can be "ab", "cd".

Example 3:
Given ["a", "aa", "aaa", "aaaa"]
Return 0
No such pair of words.
"""
__author__ = 'Daniel'


c_ Solution(object):
    ___ maxProduct(self, words):
        """
        Brute force: O(n*n*k)
        Encode string using bit manipulation
        :type words: List[str]
        :rtype: int
        """
        l = map(l.., words)
        codes = map(encode, words)
        maxa = 0
        ___ i __ xrange(l..(codes)):
            ___ j __ xrange(i+1, l..(codes)):
                __ codes[i] & codes[j] __ 0:
                    maxa = max(maxa, l[i]*l[j])

        r.. maxa

    ___ encode(self, x):
        ret = 0
        ___ c __ x:
            ret |= 1 << (ord(c)-ord('a'))
        r.. ret


__ _______ __ _______
    ... Solution().maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]) __ 16