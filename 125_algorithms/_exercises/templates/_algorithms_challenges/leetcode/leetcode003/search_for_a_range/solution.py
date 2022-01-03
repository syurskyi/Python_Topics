"""
Given a sorted array of integers, find the starting and ending position of a
given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""

c_ Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    ___ searchRange(self, A, target):
        n = l..(A)
        __ n __ 1:
            __ A[0] __ target:
                r.. [0, 0]
            ____:
                r.. [-1, -1]
        left = 0
        right = n - 1
        lower = -1
        upper = -1
        # Find lower bound
        w.... left <= right:
            mid = (left + right) / 2
            __ mid < n - 1 a.. A[mid + 1] __ target a.. A[mid] < target:
                lower = mid + 1
                break
            ____ A[mid] __ target a.. mid __ 0:
                lower = mid
                break
            ____ target <= A[mid]:
                right = mid - 1
            ____:
                left = mid + 1
        # Find upper bound
        left = 0
        right = n - 1
        w.... left <= right:
            mid = (left + right) / 2
            __ mid < n - 1 a.. A[mid + 1] > target a.. A[mid] __ target:
                upper = mid
                break
            ____ A[mid] __ target a.. mid __ n - 1:
                upper = mid
                break
            ____ target < A[mid]:
                right = mid - 1
            ____:
                left = mid + 1
        r.. [lower, upper]
