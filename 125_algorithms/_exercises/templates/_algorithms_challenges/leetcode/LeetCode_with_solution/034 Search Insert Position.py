"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it
would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 -> 2
[1,3,5,6], 2 -> 1
[1,3,5,6], 7 -> 4
[1,3,5,6], 0 -> 0
"""
__author__ = 'Danyang'
c_ Solution:
    ___ searchInsert_complex  A, target
        """
        binary search
        iterative solution
        :param A: a list of integers
        :param target: an integer to be inserted
        :return: integer
        """
        length = l..(A)
        __ n.. A o. length__0:
            r.. 0

        start = 0
        end = length -1
        # while start<=end:
        w... T...
            mid = (start+end)/2
            __ target__A[mid]:
                r.. mid
            ____ target<A[mid]:
                end = mid-1
                __ n.. start<=end:
                    # return end if end>=0 else 0
                    r.. mid __ mid>=0 ____ 0
            ____
                start = mid+1
                __ n.. start<=end:
                    r.. start

    ___ searchInsert  A, target
        """
        binary search
        iterative solution
        :param A: a list of integers
        :param target: an integer to be inserted
        :return: integer
        """
        length = l..(A)
        __ n.. A o. length__0:
            r.. 0

        start = 0
        end = length
        w.... start<end:
            mid = (start + end) / 2
            __ target__A[mid]:
                r.. mid
            ____ target<A[mid]:
                end = mid
            ____
                start = mid + 1

        r.. start

__ _____ __ ____
    ... Solution().searchInsert([1, 3, 5, 6], 5)__2
    ... Solution().searchInsert([1, 3, 5, 6], 2)__1
    ... Solution().searchInsert([1, 3, 5, 6], 7)__4
    ... Solution().searchInsert([1, 3, 5, 6], 0)__0



