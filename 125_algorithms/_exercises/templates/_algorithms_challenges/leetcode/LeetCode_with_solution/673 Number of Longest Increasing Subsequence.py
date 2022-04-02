#!/usr/bin/python3
"""
Given an unsorted array of integers, find the number of longest increasing
subsequence.

Example 1:
Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and
[1, 3, 5, 7].
Example 2:
Input: [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and
there are 5 subsequences' length is 1, so output 5.
Note: Length of the given array will be not exceed 2000 and the answer is
guaranteed to be fit in 32-bit signed int.
"""
____ typing _______ List


c_ LenCnt:
    ___ - , l, c
        l = l
        c = c

    ___  -r
        r.. repr((l, c))


c_ Solution:
    ___ findNumberOfLIS  A: List[i..]) __ i..:
        """
        Two pass - 1st pass find the LIS, 2nd pass find the number
        Let F[i] be the length of LIS ended at A[i]
        """
        __ n.. A:
            r.. 0

        n = l..(A)
        F = [LenCnt(l=1, c=1) ___ _ __ A]
        mx = LenCnt(l=1, c=1)
        ___ i __ r..(1, n
            ___ j __ r..(i
                __ A[i] > A[j]:
                    __ F[i].l < F[j].l + 1:
                        F[i].l = F[j].l + 1
                        F[i].c = F[j].c
                    ____ F[i].l __ F[j].l + 1:
                        F[i].c += F[j].c

            __ F[i].l > mx.l:
                # mx = F[i]  error, need deep copy
                mx.l = F[i].l
                mx.c = F[i].c
            ____ F[i].l __ mx.l:
                mx.c += F[i].c

        r.. mx.c


__ _______ __ _______
    ... Solution().findNumberOfLIS([1,1,1,2,2,2,3,3,3]) __ 27
    ... Solution().findNumberOfLIS([1, 3, 5, 4, 7]) __ 2
    ... Solution().findNumberOfLIS([2, 2, 2, 2, 2]) __ 5
