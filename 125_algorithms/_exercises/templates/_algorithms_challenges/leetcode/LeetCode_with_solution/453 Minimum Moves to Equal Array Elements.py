#!/usr/bin/python3
"""
Given a non-empty integer array of size n, find the minimum number of moves
required to make all array elements equal, where a move is incrementing n - 1
elements by 1.
"""


c_ Solution:
    ___ minMoves(self, nums):
        """
        List out, find the pattern
        for every operation, the max number does not change, then bring the min
        number 1 step closer to the max.

        :type nums: List[int]
        :rtype: int
        """
        mini = m..(nums)
        r.. s..(map(l.... e: e - mini, nums))


__ __name__ __ "__main__":
    ... Solution().minMoves([1, 2, 3]) __ 3
