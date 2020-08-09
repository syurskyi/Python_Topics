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


class Solution(object
    ___ maxProduct(self, words
        """
        Brute force: O(n*n*k)
        Encode string using bit manipulation
        :type words: List[str]
        :rtype: int
        """
        l = map(le., words)
        codes = map(self.encode, words)
        maxa = 0
        ___ i in xrange(le.(codes)):
            ___ j in xrange(i+1, le.(codes)):
                __ codes[i] & codes[j] __ 0:
                    maxa = max(maxa, l[i]*l[j])

        r_ maxa

    ___ encode(self, x
        ret = 0
        ___ c in x:
            ret |= 1 << (ord(c)-ord('a'))
        r_ ret


__ __name__ __ "__main__":
    assert Solution().maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]) __ 16