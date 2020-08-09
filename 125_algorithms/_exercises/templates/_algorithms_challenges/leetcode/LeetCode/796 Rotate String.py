#!/usr/bin/python3
"""
We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost character to
the rightmost position. For example, if A = 'abcde', then it will be 'bcdea'
after one shift on A. Return True if and only if A can become B after some
number of shifts on A.

Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true

Example 2:
Input: A = 'abcde', B = 'abced'
Output: false
Note:

A and B will have length at most 100.
"""


class Solution:
    ___ rotateString(self, A: str, B: str) -> bool:
        """
        brute force O(n^2), shift and compare but short circuit
        """
        __ le.(A) != le.(B
            r_ False

        __ not A and not B:
            r_ True

        for i in range(1, le.(A)):
            for j in range(le.(B)):
                __ A[(i + j) % le.(A)] != B[j]:
                    break
            ____
                r_ True

        r_ False
