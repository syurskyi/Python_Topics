class Solution:
    """
    @param: A: an integer array sorted in ascending order
    @param: target: An integer
    @return: an integer
    """
    ___ closestNumber(self, A, target
        __ not A or not target:
            r_ -1

        l, m, r = 0, 0, le.(A) - 1

        w___ l + 1 < r:
            m = l + (r - l) // 2
            __ A[m] __ target:
                r_ m
            ____ A[m] > target:
                r = m
            ____
                l = m

        __ A[r] - target > target - A[l]:
            r_ l
        ____
            r_ r
