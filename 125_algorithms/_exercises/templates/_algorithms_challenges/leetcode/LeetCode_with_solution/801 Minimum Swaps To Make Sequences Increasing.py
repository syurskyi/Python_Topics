#!/usr/bin/python3
"""
We have two integer sequences A and B of the same non-zero length.

We are allowed to swap elements A[i] and B[i].  Note that both elements are in
the same index position in their respective sequences.

At the end of some number of swaps, A and B are both strictly increasing.
(A sequence is strictly increasing if and only if A[0] < A[1] < A[2] < ... <
A[A.length - 1].)

Given A and B, return the minimum number of swaps to make both sequences
strictly increasing.  It is guaranteed that the given input always makes it
possible.

Example:
Input: A = [1,3,5,4], B = [1,2,3,7]
Output: 1
Explanation:
Swap A[3] and B[3].  Then the sequences are:
A = [1, 3, 5, 7] and B = [1, 2, 3, 4]
which are both strictly increasing.
Note:

A, B are arrays with the same length, and that length will be in the range
[1, 1000].
A[i], B[i] are integer values in the range [0, 2000].
"""


c_ Solution:
    ___ minSwap  A: L..[i..], B: L..[i..]) __ i..:
        """
        Let F[0][i] be number of swaps to make satisfy if not swap A[i], B[i]
        Let F[1][i] be ... if swap A[i], B[i]

        There is a binary array [0, 1, ...] to denote whether to swap A[i], B[i]
        without actually swapping the array
        """
        n = l..(A)
        F = [[0 ___ _ __ r..(n)] ___ _ __ r..(2)]
        F[1][0] = 1
        ___ i __ r..(1, n
            __ A[i] > m..(A[i-1], B[i-1]) a.. B[i] > m..(A[i-1], B[i-1]
                # freedom of two options - swap or not swap
                F[0][i] = m..(F[0][i-1], F[1][i-1])
                F[1][i] = m..(F[0][i-1], F[1][i-1]) + 1
            ____ A[i] > A[i-1] a.. B[i] > B[i-1]:
                # elif meaning that has to stick with previous swap choice
                # A[i] <= B[i-1] and B[i] <=A[i-1], cannot flip
                F[0][i] = F[0][i-1]
                F[1][i] = F[1][i-1] + 1
            ____:
                # has to swap, flip 
                F[0][i] = F[1][i-1]
                F[1][i] = F[0][i-1] + 1

        r.. m..(F[0][n-1], F[1][n-1])

    ___ minSwap_error  A: L..[i..], B: L..[i..]) __ i..:
        """
        for length 2
        swap A[0] and B[0] is the same as swapping A[1], B[2]
        for length 3
        it is different
        1 10 19
        3 2  8
        swap can be length - times (swap the other)
        """
        t = 0
        ___ i __ r..(1, l..(A)):
            __ A[i] <= A[i-1] o. B[i] <= B[i-1]:
                t += 1
                __ t < i + 1 - t:
                    A[i], B[i] = B[i], A[i]
                ____:
                    t = i + 1 - t

        r.. t


__ _______ __ _______
    ... Solution().minSwap([0,4,4,5,9], [0,1,6,8,10])
