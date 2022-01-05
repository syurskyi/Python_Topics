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
____ typing _______ List


c_ Solution:
    ___ longestMountain  A: List[i..]) __ i..:
        """
        dp
        """
        ret = 0
        up_cnt = 0
        down_cnt = 0
        ___ i __ r..(1, l..(A)):
            __ down_cnt a.. A[i] >= A[i-1]:
                up_cnt = 0
                down_cnt = 0
            __ A[i] > A[i-1]:
                up_cnt += 1
            ____ A[i] < A[i-1]:
                down_cnt += 1
            __ up_cnt a.. down_cnt:
                ret = m..(ret, up_cnt + down_cnt + 1)

        r.. ret

    ___ longestMountain  A: List[i..]) __ i..:
        """
        dp
        """
        n = l..(A)
        U = [0 ___ _ __ A]  # up counter from left to right
        D = [0 ___ _ __ A]  # down counter from right to left
        ___ i __ r..(1, n):
            __ A[i] > A[i-1]:
                U[i] = U[i-1] + 1
        ___ i __ r..(n-2, -1, -1):
            __ A[i] > A[i+1]:
                D[i] = D[i+1] + 1

        ret = 0
        ___ i __ r..(n):
            __ U[i] > 0 a.. D[i] > 0:
                ret = m..(ret, U[i] + D[i] + 1)

        r.. ret

    ___ longestMountain_complicated  A: List[i..]) __ i..:
        """
        a flag to indicate expecting increase or decrease
        one-pass can
        """
        ret = 0
        l = 1
        expect_incr = T..
        ___ i __ r..(1, l..(A)):
            __ expect_incr:
                __ A[i] > A[i-1]:
                    l += 1
                ____ A[i] < A[i-1] a.. l >= 2:
                    expect_incr = F..
                    l += 1
                    ret = m..(ret, l)
                ____:
                    l = 1

            ____:
                __ A[i] < A[i-1]:
                    l += 1
                    ret = m..(ret, l)
                ____ A[i] __ A[i-1]:
                    expect_incr = T..
                    l = 1
                ____:
                    expect_incr = T..
                    l = 2

        r.. ret __ ret >= 3 ____ 0


__ _______ __ _______
    ... Solution().longestMountain([2,1,4,7,3,2,5]) __ 5
    ... Solution().longestMountain([9,8,7,6,5,4,3,2,1,0]) __ 0
