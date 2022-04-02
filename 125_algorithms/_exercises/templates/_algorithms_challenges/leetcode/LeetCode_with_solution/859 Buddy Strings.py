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
USED = T..


c_ Solution:
    ___ buddyStrings  A: s.., B: s..) __ b..:
        """
        iterate
        """
        __ l..(A) != l..(B
            r.. F..
        __ A __ B:
            # find dup
            seen = s..()
            ___ a __ A:
                __ a __ seen:
                    r.. T..
                seen.add(a)
            ____:
                r.. F..

        # Find a pair
        pair = N..
        ___ i __ r..(l..(A)):
            __ A[i] != B[i]:
                __ n.. pair:
                    pair = (A[i], B[i])
                ____ pair __ (B[i], A[i]
                    pair = USED
                ____:
                    r.. F..

        __ pair __ N.. o. pair __ USED:
            r.. T..

        r.. F..
