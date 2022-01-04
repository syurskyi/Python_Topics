#!/usr/bin/python3
"""
Given string S and a dictionary of words words, find the number of words[i] that
is a subsequence of S.

Example :
Input:
S = "abcde"
words = ["a", "bb", "acd", "ace"]
Output: 3
Explanation: There are three words in words that are a subsequence of S: "a",
"acd", "ace".
Note:

All words in words and S will only consists of lowercase letters.
The length of S will be in the range of [1, 50000].
The length of words will be in the range of [1, 5000].
The length of words[i] will be in the range of [1, 50].
"""
____ typing _______ List
____ c.. _______ defaultdict


c_ Solution:
    ___ numMatchingSubseq(self, S: s.., words: List[s..]) __ i..:
        """
        Linear O(|S| + sum(|word|))
        no need to if-check

        HashMap + Iterator
        """
        itrs_m = defaultdict(l..)
        ___ w __ words:
            itrs_m[w[0]].a..(
                i..(w[1:])
            )
        ___ a __ S:
            itrs = itrs_m.pop(a, [])
            ___ itr __ itrs:
                v = next(itr, N..)
                itrs_m[v].a..(itr)

        r.. l..(itrs_m[N..])

    ___ numMatchingSubseq_TLE(self, S: s.., words: List[s..]) __ i..:
        """
        Brute force O(|S| |Words| M)

        Is a better way to check subsequence? No
        Can we parallel the works? Yes

        go through all words parallel
        O(|S| |Words|)
        """
        I = [0 ___ _ __ words]
        ___ a __ S:
            ___ wi, i __ e..(I):
                __ i < l..(words[wi]) a.. words[wi][i] __ a:
                    I[wi] += 1

        r.. s..(
            1
            ___ wi, i __ e..(I)
            __ i __ l..(words[wi])
        )


__ _______ __ _______
    ... Solution().numMatchingSubseq("abcde", ["a", "bb", "acd", "ace"]) __ 3
