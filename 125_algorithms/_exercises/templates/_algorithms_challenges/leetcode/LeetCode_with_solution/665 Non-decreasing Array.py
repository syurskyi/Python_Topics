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


class Solution:
    ___ checkPossibility(self, A: List[int]) -> bool:
        """
        greedy change
        two way of changing
        """
        changed = False
        ___ i __ r..(l..(A) - 1):
            __ A[i] <= A[i + 1]:
                continue
            __ n.. changed:
                __ i - 1 < 0 o. A[i-1] <= A[i+1]:
                    A[i] = A[i+1]
                ____:
                    A[i+1] = A[i]
                changed = True
            ____:
                r.. False

        r.. True

    ___ checkPossibility_error(self, A: List[int]) -> bool:
        """
        greedy change
        """
        changed = False
        ___ i __ r..(l..(A) - 1):
            __ A[i] <= A[i + 1]:
                continue
            __ n.. changed:
                A[i] = A[i + 1]  # Error
                __ i - 1 < 0 o. A[i - 1] <= A[i]:
                    changed = True
                ____:
                    r.. False
            ____:
                r.. False

        r.. True


__ __name__ __ "__main__":
    ... Solution().checkPossibility([4,2,3]) __ True
    ... Solution().checkPossibility([3,4,2,3]) __ False
    ... Solution().checkPossibility([2,3,3,2,4]) __ True
