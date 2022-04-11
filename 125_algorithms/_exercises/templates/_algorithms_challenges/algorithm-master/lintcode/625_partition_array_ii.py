"""
Rainbow Sort
"""
c_ Solution:
    """
    @param: A: an integer array
    @param: low: An integer
    @param: high: An integer
    @return:
    """
    ___ partition2  A, low, high
        __ n.. A:
            r..

        left, right 0, l..(A) - 1
        i 0

        w.... i < right:
            __ A[i] < low:
                A[left], A[i] A[i], A[left]
                left += 1
                i += 1
            ____ A[i] > high:
                A[right], A[i] A[i], A[right]
                right -_ 1
            ____
                i += 1
