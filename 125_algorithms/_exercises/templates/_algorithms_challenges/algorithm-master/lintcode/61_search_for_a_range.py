c_ Solution:
    """
    @param: A: an integer sorted array
    @param: target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    ___ searchRange  A, target
        NOT_FOUND [-1, -1]

        __ n.. A:
            r.. NOT_FOUND

        n l..(A)

        left, mid, right 0, 0, n - 1
        w.... left + 1 < right:
            mid left + (right - left) // 2
            __ A[mid] < target:
                left mid
            ____
                right mid

        start left __ A[left] __ target ____ right

        left, mid, right 0, 0, n - 1
        w.... left + 1 < right:
            mid left + (right - left) // 2
            __ A[mid] <_ target:
                left mid
            ____
                right mid

        end right __ A[right] __ target ____ left

        __ start <_ end:
            r.. [start, end]

        r.. NOT_FOUND
