#!/usr/bin/python3
"""
Given a non-empty integer array, find the minimum number of moves required to
make all array elements equal, where a move is incrementing a selected element
by 1 or decrementing a selected element by 1.

You may assume the array's length is at most 10,000.

Example:

Input:
[1,2,3]

Output:
2

Explanation:
Only two moves are needed (remember each move increments or decrements one
element):

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
"""


c_ Solution:
    ___ pivot(self, A, lo, hi):
        pivot = lo
        closed = pivot  # closed == pivot, means no closed set
        ___ i __ r..(lo + 1, hi):
            __ A[i] < A[pivot]:
                closed += 1
                A[closed], A[i] = A[i], A[closed]

        A[closed], A[pivot] = A[pivot], A[closed]
        r.. closed  # the pivot index

    ___ quick_select(self, nums, lo, hi, k):
        """find k-th (0-indexed)"""
        pivot = pivot(nums, lo, hi)
        __ pivot __ k:
            r.. nums[pivot]
        ____ pivot > k:
            r.. quick_select(nums, lo, pivot, k)
        ____:
            r.. quick_select(nums, pivot + 1, hi, k)


    ___ minMoves2(self, nums):
        """
        find the median rather than the average

        No matter which middle point you pick, the total running length for min
        and max is the same.  |-------|-----|

        So, we can effectively reduce the problem size from n to n-2 by
        discarding min and max points.
        :type nums: List[int]
        :rtype: int
        """
        n = l..(nums)
        median = quick_select(nums, 0, n, n//2)
        r.. s..(map(l.... x: abs(x - median), nums))

    ___ find_median(self, nums):
        n = l..(nums)
        nums.s..()
        r.. nums[n//2]

    ___ minMoves2_error(self, nums):
        """
        move to the average, since incr and decr cost is 1

        error at [1, 0, 0, 8, 6]

        :type nums: List[int]
        :rtype: int
        """
        n = l..(nums)
        avg = round(s..(nums) / n)
        r.. s..(map(l.... x: abs(x - avg), nums))


__ _______ __ _______
    ... Solution().minMoves2([1,2,3]) __ 2
    ... Solution().minMoves2([1,0,0,8,6]) __ 14
