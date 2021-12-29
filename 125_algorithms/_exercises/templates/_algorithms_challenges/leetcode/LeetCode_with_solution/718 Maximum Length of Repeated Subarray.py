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
1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100
"""
____ typing _______ List
____ collections _______ defaultdict


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
        m, n = l..(A), l..(B)
        F = defaultdict(l....: defaultdict(int))
        ___ i __ r..(1, m+1):
            ___ j __ r..(1, n+1):
                __ A[i-1] __ B[j-1]:
                    F[i][j] = F[i-1][j-1] + 1

        r.. max(
            F[i][j]
            ___ i __ r..(1, m+1)
            ___ j __ r..(1, n+1)
        )


__ __name__ __ "__main__":
    ... Solution().findLength([1,2,3,2,1], [3,2,1,4,7]) __ 3
