c_ Solution:
    """
    @param: A: A list of integer which is 0, 1 or 2
    @return: nothing
    """
    ___ sortColors  A
        __ n.. A:
            r..

        left, right = 0, l..(A) - 1
        i = 0
        w.... i <_ right:
            __ A[i] __ 0:
                A[left], A[i] = A[i], A[left]
                left += 1
                i += 1
            ____ A[i] __ 1:
                """
                temply ignore it
                it will be swapped if there is `0` later
                """
                i += 1
            ____
                """
                cannot `i += 1` since the swapped value still need to check
                """
                A[right], A[i] = A[i], A[right]
                right -_ 1
