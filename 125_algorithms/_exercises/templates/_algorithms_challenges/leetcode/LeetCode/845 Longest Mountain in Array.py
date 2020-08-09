#!/usr/bin/python3
"""
Let's call any (contiguous) subarray B (of A) a mountain if the following
properties hold:

B.length >= 3
There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] <
B[i] > B[i+1] > ... > B[B.length - 1]
(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain.

Return 0 if there is no mountain.

Example 1:

Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
Example 2:

Input: [2,2,2]
Output: 0
Explanation: There is no mountain.
Note:

0 <= A.length <= 10000
0 <= A[i] <= 10000
Follow up:

Can you solve it using only one pass?
Can you solve it in O(1) space?
"""
from typing ______ List


class Solution:
    ___ longestMountain(self, A: List[int]) -> int:
        """
        dp
        """
        ret = 0
        up_cnt = 0
        down_cnt = 0
        ___ i in range(1, le.(A)):
            __ down_cnt and A[i] >= A[i-1]:
                up_cnt = 0
                down_cnt = 0
            __ A[i] > A[i-1]:
                up_cnt += 1
            ____ A[i] < A[i-1]:
                down_cnt += 1
            __ up_cnt and down_cnt:
                ret = max(ret, up_cnt + down_cnt + 1)

        r_ ret

    ___ longestMountain(self, A: List[int]) -> int:
        """
        dp
        """
        n = le.(A)
        U = [0 ___ _ in A]  # up counter from left to right
        D = [0 ___ _ in A]  # down counter from right to left
        ___ i in range(1, n
            __ A[i] > A[i-1]:
                U[i] = U[i-1] + 1
        ___ i in range(n-2, -1, -1
            __ A[i] > A[i+1]:
                D[i] = D[i+1] + 1

        ret = 0
        ___ i in range(n
            __ U[i] > 0 and D[i] > 0:
                ret = max(ret, U[i] + D[i] + 1)

        r_ ret

    ___ longestMountain_complicated(self, A: List[int]) -> int:
        """
        a flag to indicate expecting increase or decrease
        one-pass can
        """
        ret = 0
        l = 1
        expect_incr = True
        ___ i in range(1, le.(A)):
            __ expect_incr:
                __ A[i] > A[i-1]:
                    l += 1
                ____ A[i] < A[i-1] and l >= 2:
                    expect_incr = False
                    l += 1
                    ret = max(ret, l)
                ____
                    l = 1

            ____
                __ A[i] < A[i-1]:
                    l += 1
                    ret = max(ret, l)
                ____ A[i] __ A[i-1]:
                    expect_incr = True
                    l = 1
                ____
                    expect_incr = True
                    l = 2

        r_ ret __ ret >= 3 else 0


__ __name__ __ "__main__":
    assert Solution().longestMountain([2,1,4,7,3,2,5]) __ 5
    assert Solution().longestMountain([9,8,7,6,5,4,3,2,1,0]) __ 0
