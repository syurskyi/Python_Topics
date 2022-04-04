c_ Solution:
    # @param A: The integer array
    # @param target: Target number to find
    # @return the first position of target in A, position start from 0
    ___ binarySearch  A, target
        __ n.. A:
            r.. -1

        left, mid, right = 0, 0, l..(A) - 1

        w.... left + 1 < right:
            mid = left + (right - left) // 2
            __ A[mid] < target:
                left = mid
            ____
                right = mid

        __ A[left] __ target:
            r.. left
        ____ A[right] __ target:
            r.. right

        r.. -1
