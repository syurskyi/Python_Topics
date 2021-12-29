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
import math


class Solution:
    ___ repeatedStringMatch(self, A, B):
        r = math.ceil(len(B) / len(A))
        for count in (r, r + 1):  # r + 1 when len(B) % len(A) == 0
            __ B in A * count:
                return count

        return -1

    ___ repeatedStringMatch_TLE(self, A: str, B: str) -> int:
        for i in range(len(A)):
            j = 0
            count = 0
            while j < len(B):
                __ i + j - count * len(A) >= len(A):
                    count += 1
                idx = i + j - count * len(A)
                __ A[idx] == B[j]:
                    j += 1
                else:
                    break

            __ j == len(B):
                return count + 1

        return -1
