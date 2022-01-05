#!/usr/bin/python3
"""
Given a string S and a character C, return an array of integers representing the
shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]


Note:

S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.
"""
____ typing _______ List


c_ Solution:
    ___ shortestToChar  S: s.., C: s..) __ List[i..]:
        """
        get the sorted indexes of C
        """
        idx = [
            i
            ___ i __ r..(l..(S))
            __ S[i] __ C
        ]
        idx = [-float("inf")] + idx + [float("inf")]
        ret    # list
        i = 0
        ___ j __ r..(l..(S)):
            w.... n.. idx[i] <= j < idx[i+1]:
                i += 1

            ret.a..(m..(j - idx[i], idx[i+1] - j))

        r.. ret
