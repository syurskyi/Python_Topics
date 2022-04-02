#!/usr/bin/python3
"""
Given an array with n integers, your task is to check if it could become
non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every
i (1 <= i < n).

Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:
Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.
Note: The n belongs to [1, 10,000].
"""
____ typing _______ List


c_ Solution:
    ___ checkPossibility  A: List[i..]) __ b..:
        """
        greedy change
        two way of changing
        """
        changed = F..
        ___ i __ r..(l..(A) - 1):
            __ A[i] <= A[i + 1]:
                _____
            __ n.. changed:
                __ i - 1 < 0 o. A[i-1] <= A[i+1]:
                    A[i] = A[i+1]
                ____:
                    A[i+1] = A[i]
                changed = T..
            ____:
                r.. F..

        r.. T..

    ___ checkPossibility_error  A: List[i..]) __ b..:
        """
        greedy change
        """
        changed = F..
        ___ i __ r..(l..(A) - 1):
            __ A[i] <= A[i + 1]:
                _____
            __ n.. changed:
                A[i] = A[i + 1]  # Error
                __ i - 1 < 0 o. A[i - 1] <= A[i]:
                    changed = T..
                ____:
                    r.. F..
            ____:
                r.. F..

        r.. T..


__ _______ __ _______
    ... Solution().checkPossibility([4,2,3]) __ T..
    ... Solution().checkPossibility([3,4,2,3]) __ F..
    ... Solution().checkPossibility([2,3,3,2,4]) __ T..
