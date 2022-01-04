#!/usr/bin/python3
"""
Given an array A of non-negative integers, return an array consisting of all the
even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.



Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.


Note:

1 <= A.length <= 5000
0 <= A[i] <= 5000
"""
____ typing _______ List


c_ Solution:
    ___ sortArrayByParity(self, A: List[i..]) __ List[i..]:
        """
        pointer
        """
        closed = -1
        ___ i __ r..(l..(A)):
            __ A[i] % 2 __ 0:
                closed += 1
                A[closed], A[i] = A[i], A[closed]

        r.. A
