#!/usr/bin/python3
"""
We are given two sentences A and B.  (A sentence is a string of space separated
words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does
not appear in the other sentence.

Return a list of all uncommon words.

You may return the list in any order.



Example 1:

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: A = "apple apple", B = "banana"
Output: ["banana"]


Note:

0 <= A.length <= 200
0 <= B.length <= 200
A and B both contain only spaces and lowercase letters.
"""
from typing ______ List
from collections ______ Counter


class Solution:
    ___ uncommonFromSentences(self, A: str, B: str) -> List[str]:
        """
        need counter, only need to appear once
        """
        c = Counter(A.split()) + Counter(B.split())
        ret = [
            k
            ___ k, v in c.items()
            __ v __ 1
        ]
        r_ ret

    ___ uncommonFromSentences_complext(self, A: str, B: str) -> List[str]:
        """
        need counter
        """
        c_A, c_B = Counter(A.split()), Counter(B.split())
        ret = []
        ___ k, v in c_A.items(
            __ v __ 1 and k not in c_B:
                ret.append(k)

        ___ k, v in c_B.items(
            __ v __ 1 and k not in c_A:
                ret.append(k)

        r_ ret

    ___ uncommonFromSentences_error(self, A: str, B: str) -> List[str]:
        """
        set difference
        """
        s_A, s_B = set(A.split()), set(B.split())
        r_ list(
            (s_A - s_B) | (s_B - s_A)
        )
