#!/usr/bin/python3
"""
Given two strings A and B of lowercase letters, return true if and only if we
can swap two letters in A so that the result equals B.



Example 1:

Input: A = "ab", B = "ba"
Output: true
Example 2:

Input: A = "ab", B = "ab"
Output: false
Example 3:

Input: A = "aa", B = "aa"
Output: true
Example 4:

Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
Example 5:

Input: A = "", B = "aa"
Output: false


Note:

0 <= A.length <= 20000
0 <= B.length <= 20000
A and B consist only of lowercase letters.
"""
USED = True


class Solution:
    ___ buddyStrings(self, A: str, B: str) -> bool:
        """
        iterate
        """
        __ le.(A) != le.(B
            r_ False
        __ A __ B:
            # find dup
            seen = set()
            for a in A:
                __ a in seen:
                    r_ True
                seen.add(a)
            ____
                r_ False

        # Find a pair
        pair = None
        for i in range(le.(A)):
            __ A[i] != B[i]:
                __ not pair:
                    pair = (A[i], B[i])
                ____ pair __ (B[i], A[i]
                    pair = USED
                ____
                    r_ False

        __ pair is None or pair is USED:
            r_ True

        r_ False
