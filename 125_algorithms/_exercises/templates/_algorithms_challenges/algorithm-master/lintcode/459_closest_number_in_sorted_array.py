class Solution:
    """
    @param: A: an integer array sorted in ascending order
    @param: target: An integer
    @return: an integer
    """
    ___ closestNumber(self, A, target):
        __ not A or not target:
            return -1

        l, m, r = 0, 0, len(A) - 1

        while l + 1 < r:
            m = l + (r - l) // 2
            __ A[m] == target:
                return m
            elif A[m] > target:
                r = m
            else:
                l = m

        __ A[r] - target > target - A[l]:
            return l
        else:
            return r
