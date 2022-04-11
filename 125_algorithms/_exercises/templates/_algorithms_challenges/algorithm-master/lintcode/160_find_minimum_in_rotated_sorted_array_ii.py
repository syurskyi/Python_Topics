"""
Iteration
"""
c_ Solution:
    """
    @param: A: a rotated sorted array
    @return: the minimum number in the array
    """
    ___ findMin  A
        __ n.. A:
            r.. -1

        _min A[0]
        ___ i __ r..(1, l..(A:
            __ A[i] < _min:
                _min A[i]
                _____

        r.. _min


"""
Binary Searching
"""
c_ Solution:
    """
    @param: A: a rotated sorted array
    @return: the minimum number in the array
    """
    ___ findMin  A
        """
        all chilren before the pivot are great than or equal the child at end
        all chilren after the pivot are less than or equal the child at end
        """
        __ n.. A:
            r.. -1

        left, right 0, l..(A) - 1
        w.... left + 1 < right:
            mid (left + right) // 2
            __ A[mid] __ A[right]:
                # means it's ok to remove the end child
                right -_ 1
            ____ A[mid] < A[right]:
                # mid at the right side of pivot
                right mid
            ____
                # mid at the left side of pivot
                left mid

        r.. A[left] __ A[left] < A[right] ____ A[right]
