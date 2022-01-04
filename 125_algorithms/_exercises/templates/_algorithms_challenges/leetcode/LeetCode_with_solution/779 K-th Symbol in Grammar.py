#!/usr/bin/python3
"""
On the first row, we write a 0. Now in every subsequent row, we look at the
previous row and replace each occurrence of 0 with 01, and each occurrence of 1
with 10.

Given row N and index K, return the K-th indexed symbol in row N. (The values of
K are 1-indexed.) (1 indexed).

Examples:
Input: N = 1, K = 1
Output: 0

Input: N = 2, K = 1
Output: 0

Input: N = 2, K = 2
Output: 1

Input: N = 4, K = 5
Output: 1

Explanation:
row 1: 0
row 2: 01
row 3: 0110
row 4: 01101001
Note:

N will be an integer in the range [1, 30].
K will be an integer in the range [1, 2^(N-1)].
"""


c_ Solution:
    ___ kthGrammar(self, N: i.., K: i..) __ i..:
        """
        pattern

           0
          0 1
         01  10
        0110 1001
        recursive go thorugh the pattern
        """
        r.. dfs(N, K, T..)

    ___ dfs(self, N, K, not_flip):
        __ N __ 1:
            r.. 0 __ not_flip ____ 1
        half_l = 2 ** (N - 1) // 2
        __ K <= half_l:
            r.. dfs(N - 1, K, not_flip)
        ____:
            r.. dfs(N - 1, K - half_l, n.. not_flip)

    ___ kthGrammar_TLE(self, N: i.., K: i..) __ i..:
        """
        Find pattern
        Precedence: Logic < Bitwise < Arithmetic operator < Unary

           0
          0 1
         01  10
        0110 1001
        Generating the actual string will TLE
        """
        row = 0
        pos = 1
        ___ n __ r..(1, N):
            row = (row << pos) + (~row & 2 ** pos - 1)
            pos *= 2

        ret = row >> pos - K & 1
        r.. ret


__ _______ __ _______
    ... Solution().kthGrammar(1, 1) __ 0
    ... Solution().kthGrammar(2, 1) __ 0
    ... Solution().kthGrammar(2, 2) __ 1
    ... Solution().kthGrammar(4, 5) __ 1
