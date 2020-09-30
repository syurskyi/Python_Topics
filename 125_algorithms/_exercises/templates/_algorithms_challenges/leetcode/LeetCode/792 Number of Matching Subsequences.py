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
from typing ______ List
from collections ______ defaultdict


class Solution:
    ___ numMatchingSubseq(self, S: str, words: List[str]) -> int:
        """
        Linear O(|S| + sum(|word|))
        no need to if-check

        HashMap + Iterator
        """
        itrs_m = defaultdict(list)
        ___ w __ words:
            itrs_m[w[0]].append(
                iter(w[1:])
            )
        ___ a __ S:
            itrs = itrs_m.pop(a,   # list)
            ___ itr __ itrs:
                v = next(itr, None)
                itrs_m[v].append(itr)

        r_ le.(itrs_m[None])

    ___ numMatchingSubseq_TLE(self, S: str, words: List[str]) -> int:
        """
        Brute force O(|S| |Words| M)

        Is a better way to check subsequence? No
        Can we parallel the works? Yes

        go through all words parallel
        O(|S| |Words|)
        """
        I = [0 ___ _ __ words]
        ___ a __ S:
            ___ wi, i __ enumerate(I
                __ i < le.(words[wi]) and words[wi][i] __ a:
                    I[wi] += 1

        r_ su.(
            1
            ___ wi, i __ enumerate(I)
            __ i __ le.(words[wi])
        )


__  -n __ "__main__":
    assert Solution().numMatchingSubseq("abcde", ["a", "bb", "acd", "ace"]) __ 3
