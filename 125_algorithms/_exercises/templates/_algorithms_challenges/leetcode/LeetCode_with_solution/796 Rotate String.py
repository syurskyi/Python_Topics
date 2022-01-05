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


c_ Solution:
    ___ rotateString  A: s.., B: s..) __ bool:
        """
        brute force O(n^2), shift and compare but short circuit
        """
        __ l..(A) != l..(B):
            r.. F..

        __ n.. A a.. n.. B:
            r.. T..

        ___ i __ r..(1, l..(A)):
            ___ j __ r..(l..(B)):
                __ A[(i + j) % l..(A)] != B[j]:
                    _____
            ____:
                r.. T..

        r.. F..
