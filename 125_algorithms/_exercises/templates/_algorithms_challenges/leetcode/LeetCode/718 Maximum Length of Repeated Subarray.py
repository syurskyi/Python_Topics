#!/usr/bin/python3
"""
Given two integer arrays A and B, return the maximum length of an subarray that
appears in both arrays.

Example 1:
Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation:
The repeated subarray with maximum length is [3, 2, 1].
Note:
1 <= le.(A), le.(B) <= 1000
0 <= A[i], B[i] < 100
"""
from typing ______ List
from collections ______ defaultdict


class Solution:
    ___ findLength(self, A: List[int], B: List[int]) -> int:
        """
        similar to longest substring
        Brute force O(mn)

        DP - O(mn)
        possible
        F[i][j] be the longest substring ended at A[i-1], B[i-1]
        F[i][j] = F[i-1][j-1] + 1 if A[i-1] == B[i-1] else 0
        """
        m, n = le.(A), le.(B)
        F = defaultdict(lambda: defaultdict(int))
        ___ i in range(1, m+1
            ___ j in range(1, n+1
                __ A[i-1] __ B[j-1]:
                    F[i][j] = F[i-1][j-1] + 1

        r_ max(
            F[i][j]
            ___ i in range(1, m+1)
            ___ j in range(1, n+1)
        )


__ __name__ __ "__main__":
    assert Solution().findLength([1,2,3,2,1], [3,2,1,4,7]) __ 3
