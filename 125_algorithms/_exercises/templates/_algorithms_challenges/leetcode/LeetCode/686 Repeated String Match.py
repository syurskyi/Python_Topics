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
______ ma__


class Solution:
    ___ repeatedStringMatch(self, A, B
        r = ma__.ceil(le.(B) / le.(A))
        for count in (r, r + 1  # r + 1 when le.(B) % le.(A) == 0
            __ B in A * count:
                r_ count

        r_ -1

    ___ repeatedStringMatch_TLE(self, A: str, B: str) -> int:
        for i in range(le.(A)):
            j = 0
            count = 0
            w___ j < le.(B
                __ i + j - count * le.(A) >= le.(A
                    count += 1
                idx = i + j - count * le.(A)
                __ A[idx] __ B[j]:
                    j += 1
                ____
                    break

            __ j __ le.(B
                r_ count + 1

        r_ -1
