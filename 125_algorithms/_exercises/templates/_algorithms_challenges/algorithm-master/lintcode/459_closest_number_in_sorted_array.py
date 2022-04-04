c_ Solution:
    """
    @param: A: an integer array sorted in ascending order
    @param: target: An integer
    @return: an integer
    """
    ___ closestNumber  A, target
        __ n.. A o. n.. target:
            r.. -1

        l, m, r = 0, 0, l..(A) - 1

        w.... l + 1 < r:
            m = l + (r - l) // 2
            __ A[m] __ target:
                r.. m
            ____ A[m] > target:
                r = m
            ____
                l = m

        __ A[r] - target > target - A[l]:
            r.. l
        ____
            r.. r
