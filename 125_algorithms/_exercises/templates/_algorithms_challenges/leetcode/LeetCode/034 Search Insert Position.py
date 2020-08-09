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
class Solution:
    ___ searchInsert_complex(self, A, target
        """
        binary search
        iterative solution
        :param A: a list of integers
        :param target: an integer to be inserted
        :return: integer
        """
        length = le.(A)
        __ not A or length__0:
            r_ 0

        start = 0
        end = length -1
        # w___ start<=end:
        w___ True:
            mid = (start+end)/2
            __ target__A[mid]:
                r_ mid
            ____ target<A[mid]:
                end = mid-1
                __ not start<=end:
                    # return end if end>=0 else 0
                    r_ mid __ mid>=0 else 0
            ____
                start = mid+1
                __ not start<=end:
                    r_ start

    ___ searchInsert(self, A, target
        """
        binary search
        iterative solution
        :param A: a list of integers
        :param target: an integer to be inserted
        :return: integer
        """
        length = le.(A)
        __ not A or length__0:
            r_ 0

        start = 0
        end = length
        w___ start<end:
            mid = (start + end) / 2
            __ target__A[mid]:
                r_ mid
            ____ target<A[mid]:
                end = mid
            ____
                start = mid + 1

        r_ start

__ __name____"__main__":
    assert Solution().searchInsert([1, 3, 5, 6], 5)__2
    assert Solution().searchInsert([1, 3, 5, 6], 2)__1
    assert Solution().searchInsert([1, 3, 5, 6], 7)__4
    assert Solution().searchInsert([1, 3, 5, 6], 0)__0



