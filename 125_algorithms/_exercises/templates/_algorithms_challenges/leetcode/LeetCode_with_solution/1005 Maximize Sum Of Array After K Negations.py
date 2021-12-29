#!/usr/bin/python3
"""
Given an array A of integers, we must modify the array in the following way: we
choose an i and replace A[i] with -A[i], and we repeat this process K times in
total.  (We may choose the same index i multiple times.)

Return the largest possible sum of the array after modifying it in this way.



Example 1:

Input: A = [4,2,3], K = 1
Output: 5
Explanation: Choose indices (1,) and A becomes [4,-2,3].
Example 2:

Input: A = [3,-1,0,2], K = 3
Output: 6
Explanation: Choose indices (1, 2, 2) and A becomes [3,1,0,2].
Example 3:

Input: A = [2,-3,-1,5,-4], K = 2
Output: 13
Explanation: Choose indices (1, 4) and A becomes [2,3,-1,5,4].


Note:

1 <= A.length <= 10000
1 <= K <= 10000
-100 <= A[i] <= 100
"""
____ typing _______ List


class Solution:
    ___ largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        """
        revert all the negative, if positive, revert multiple times the smallest

        since -100 <= A[i] <= 100, then sort can be done in linear time
        """
        A.sort()
        ___ i __ r..(l..(A)):
            __ K __ 0:
                break

            __ A[i] < 0:
                A[i] *= -1
                prev = A[i]
                K -= 1
            ____:
                __ K % 2 != 0:
                    __ i - 1 >= 0 and A[i-1] < A[i]:
                        A[i-1] *= -1
                    ____:
                        A[i] *= -1
                break

        r.. s..(A)
