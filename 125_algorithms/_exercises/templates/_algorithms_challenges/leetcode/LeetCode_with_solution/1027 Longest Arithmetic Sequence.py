#!/usr/bin/python3
"""
Given an array A of integers, return the length of the longest arithmetic
subsequence in A.

Recall that a subsequence of A is a list A[i_1], A[i_2], ..., A[i_k] with
0 <= i_1 < i_2 < ... < i_k <= A.length - 1, and that a sequence B is arithmetic
if B[i+1] - B[i] are all the same value (for 0 <= i < B.length - 1).

Example 1:
Input: [3,6,9,12]
Output: 4
Explanation:
The whole array is an arithmetic sequence with steps of length = 3.

Example 2:
Input: [9,4,7,2,10]
Output: 3
Explanation:
The longest arithmetic subsequence is [4,7,10].

Example 3:
Input: [20,1,15,3,10,5,8]
Output: 4
Explanation:
The longest arithmetic subsequence is [20,15,10,5].

Note:
2 <= A.length <= 2000
0 <= A[i] <= 10000
"""
____ typing _______ List
____ c.. _______ d..


c_ Solution:
    ___ longestArithSeqLength  A: List[i..]) __ i..:
        """
        Brute force O(n^2)

        Let F[i][j] be the longest arith subseq ending at A[i] with step j
        """
        F = d..(l....: d..(l....: 1))
        ___ i __ r..(l..(A)):
            ___ j __ r..(i
                delta = A[i] - A[j]
                F[i][delta] = F[j][delta] + 1

        ret = 0
        ___ d __ F.v..
            ___ v __ d.v..
                ret = m..(ret, v)

        r.. ret


__ _______ __ _______
    ... Solution().longestArithSeqLength([20,1,15,3,10,5,8]) __ 4
