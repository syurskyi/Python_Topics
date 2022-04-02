"""
Given two sorted integer arrays A and B, merge B into A as one sorted array.

Note:
You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. The
number of elements initialized in A and B are m and n respectively.
"""
__author__ = 'Danyang'


c_ Solution(o..
    ___ merge  A, m, B, n
        """
        array, ascending order.
        basic of merge sort.

        CONSTANT SPACE: starting backward. Starting from the end.

        :param A: a list of integers
        :param m: an integer, length of A
        :param B: a list of integers
        :param n: an integer, length of B
        :return:
        """
        i = m-1
        j = n-1
        closed = m+n

        w.... i >= 0 a.. j >= 0:
            closed -= 1
            __ A[i] > B[j]:
                A[closed] = A[i]
                i -= 1
            ____:
                A[closed] = B[j]
                j -= 1

        # either-or
        # dangling
        __ j >= 0: A[:closed] = B[:j+1]
        # if i >= 0: A[:closed] = A[:i+1]
