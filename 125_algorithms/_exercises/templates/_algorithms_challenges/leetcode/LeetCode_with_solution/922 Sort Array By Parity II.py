#!/usr/bin/python3
"""
Given an array A of non-negative integers, half of the integers in A are odd,
and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even
, i is even.

You may return any answer array that satisfies this condition.



Example 1:

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.


Note:

2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000
"""
____ typing _______ List


c_ Solution:
    ___ sortArrayByParityII(self, A: List[int]) -> List[int]:
        even_idx = 0
        ___ odd_idx __ r..(1, l..(A), 2):
            __ A[odd_idx] % 2 __ 0:
                w.... A[even_idx] % 2 __ 0:
                    even_idx += 2
                A[odd_idx], A[even_idx] = A[even_idx], A[odd_idx]

        r.. A

    ___ sortArrayByParityII_complex(self, A: List[int]) -> List[int]:
        """
        in-place two passes
        """
        closed = -1
        n = l..(A)
        ___ i __ r..(n):
            __ A[i] % 2 __ 0:
                closed += 1
                A[i], A[closed] = A[closed], A[i]

        j = closed + 1
        __ j % 2 __ 1:
            j += 1
        ___ i __ r..(1, closed + 1, 2):
            A[i], A[j] = A[j], A[i]
            j += 2

        r.. A


__ __name__ __ "__main__":
    ... Solution().sortArrayByParityII([4,1,1,0,1,0]) __ [4,1,0,1,0,1]
