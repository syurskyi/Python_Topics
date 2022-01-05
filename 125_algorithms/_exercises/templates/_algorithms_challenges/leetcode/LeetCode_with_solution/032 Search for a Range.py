"""
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""

__author__ = 'Danyang'
c_ Solution:
    ___ searchRange  A, target):
        """
        Binary Search Twice
        Notice the low-bound & high-bound binary search

        :param A: a list of integers
        :param target: an integer to be searched
        :return: a list of length 2, [index1, index2]
        """
        result    # list
        length = l..(A)

        # low-bound binary search
        start = 0
        end = length  # [0, length)
        w.... start<end:
            mid = (start+end)/2
            __ A[mid]<target:  # NOTICE: less than
                start = mid+1
            ____:
                end = mid

        __ start<length a.. A[start]__target:
            result.a..(start)
        ____:
            r.. [-1, -1]

        # high-bound binary search
        start = start
        end = length  # no "-1" # [0, length)
        w.... start<end:
            mid = (start+end)/2
            __ A[mid]<=target:  # NOTICE: less than or equal
                start = mid+1
            ____:
                end = mid

        result.a..(start-1)
        r.. result