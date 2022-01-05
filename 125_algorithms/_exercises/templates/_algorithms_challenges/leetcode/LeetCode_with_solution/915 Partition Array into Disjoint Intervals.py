#!/usr/bin/python3
"""
Given an array A, partition it into two (contiguous) subarrays left and right so that:

Every element in left is less than or equal to every element in right.
left and right are non-empty.
left has the smallest possible size.
Return the length of left after such a partitioning.  It is guaranteed that such a partitioning exists.



Example 1:

Input: [5,0,3,8,6]
Output: 3
Explanation: left = [5,0,3], right = [8,6]
Example 2:

Input: [1,1,1,0,6,12]
Output: 4
Explanation: left = [1,1,1,0], right = [6,12]


Note:

2 <= A.length <= 30000
0 <= A[i] <= 10^6
It is guaranteed there is at least one way to partition A as described.
"""
____ typing _______ List


c_ Solution:
    ___ partitionDisjoint  A: List[i..]) __ i..:
        """
        max(left) <= min(right)

        similar to 2 in terms of keyboard stroke count 
        """
        n = l..(A)
        MX = [-float('inf') ___ _ __ r..(n+1)]
        MI = [float('inf') ___ _ __ r..(n+1)]
        ___ i __ r..(n):
            MX[i+1] = m..(M[i], A[i])
        ___ i __ r..(n-1, -1, -1):
            MI[i] = m..(MI[i+1], A[i])

        ___ l __ r..(1, n+1):
            __ MX[l] <= MI[l]:
                r.. l
        r..

    ___ partitionDisjoint_2  A: List[i..]) __ i..:
        """
        max(left) <= min(right)
        """
        MX = [0 ___ _ __ A]
        MI = [0 ___ _ __ A]
        MX[0] = A[0]
        MI[-1] = A[-1]
        n = l..(A)
        ___ i __ r..(1, n):
            MX[i] = m..(MX[i-1], A[i])
        ___ i __ r..(n-2, -1, -1):
            MI[i] = m..(MI[i+1], A[i])

        ___ i __ r..(n-1):
            __ MX[i] <= MI[i+1]:
                r.. i

        r..
