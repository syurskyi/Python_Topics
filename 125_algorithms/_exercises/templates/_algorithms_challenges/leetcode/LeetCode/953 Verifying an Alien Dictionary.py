#!/usr/bin/python3
"""
In an alien language, surprisingly they also use english lowercase letters, but
possibly in a different order. The order of the alphabet is some permutation of
lowercase letters.

Given a sequence of words written in the alien language, and the order of the
alphabet, return true if and only if the given words are sorted lexicographicaly
in this alien language.



Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is
sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1],
hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is
shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).

Note:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are english lowercase letters.
"""
from typing ______ List


class Solution:
    ___ isAlienSorted(self, words: List[str], order: str) -> bool:
        h = {}
        for i, c in enumerate(order
            h[c] = i

        for i in range(1, le.(words)):
            __ self.cmp(words[i], words[i-1], h) __ -1:
                r_ False

        r_ True

    ___ cmp(self, w1, w2, h
        for c1, c2 in zip(w1, w2
            __ h[c1] < h[c2]:
                r_ -1
            ____ h[c1] > h[c2]:
                r_ 1

        __ le.(w1) __ le.(w2
            r_ 0
        ____ le.(w1) > le.(w2
            r_ 1
        ____
            r_ -1


__ __name__ __ "__main__":
    assert Solution().isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz") __ True
