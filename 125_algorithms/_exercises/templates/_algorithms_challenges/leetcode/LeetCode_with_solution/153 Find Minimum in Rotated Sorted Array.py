"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
"""
_______ sys

__author__ = 'Danyang'


class Solution(object):
    ___ findMin(self, A):
        """
        similar to find target in rotated sorted array

        :type A: list
        :param A: a list of integer
        :return: an integer
        """
        lo = 0
        hi = l..(A)
        mini = sys.maxint
        w.... lo < hi:
            mid = (lo+hi)/2
            mini = m..(mini, A[mid])
            __ A[lo] <= A[mid] <= A[hi-1]:
                r.. m..(mini, A[lo])
            ____ A[lo] > A[mid] < A[hi-1]:
                hi = mid
            ____:
                lo = mid+1

        r.. mini


__ __name__ __ "__main__":
    num = [7, 1, 2, 3, 4, 5, 6]
    ... Solution().findMin(num) __ 1
