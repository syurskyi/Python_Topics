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
____ typing _______ List


c_ Solution:
    ___ isAlienSorted  words: List[s..], order: s..) __ b..:
        h    # dict
        ___ i, c __ e..(order
            h[c] = i

        ___ i __ r..(1, l..(words)):
            __ cmp(words[i], words[i-1], h) __ -1:
                r.. F..

        r.. T..

    ___ cmp  w1, w2, h
        ___ c1, c2 __ z..(w1, w2
            __ h[c1] < h[c2]:
                r.. -1
            ____ h[c1] > h[c2]:
                r.. 1

        __ l..(w1) __ l..(w2
            r.. 0
        ____ l..(w1) > l..(w2
            r.. 1
        ____:
            r.. -1


__ _______ __ _______
    ... Solution().isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz") __ T..
