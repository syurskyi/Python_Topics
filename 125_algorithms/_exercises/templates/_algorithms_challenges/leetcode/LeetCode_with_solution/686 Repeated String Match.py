#!/usr/bin/python3
"""
Given two strings A and B, find the minimum number of times A has to be repeated
such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring
of it; and B is not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.
"""
_______ math


c_ Solution:
    ___ repeatedStringMatch  A, B):
        r = math.ceil(l..(B) / l..(A))
        ___ count __ (r, r + 1):  # r + 1 when len(B) % len(A) == 0
            __ B __ A * count:
                r.. count

        r.. -1

    ___ repeatedStringMatch_TLE  A: s.., B: s..) __ i..:
        ___ i __ r..(l..(A)):
            j = 0
            count = 0
            w.... j < l..(B):
                __ i + j - count * l..(A) >= l..(A):
                    count += 1
                idx = i + j - count * l..(A)
                __ A[idx] __ B[j]:
                    j += 1
                ____:
                    _____

            __ j __ l..(B):
                r.. count + 1

        r.. -1
