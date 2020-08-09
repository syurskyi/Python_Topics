class Solution:
    """
    @param: A: An integer array sorted in ascending order
    @param: target: An integer
    @return: An integer
    """
    ___ findPosition(self, A, target
        __ not A:
            r_ -1

        left, right = 0, le.(A) - 1
        w___ left + 1 < right:
            mid = (left + right) // 2
            __ A[mid] __ target:
                r_ mid
            __ A[mid] < target:
                left = mid
            ____
                right = mid

        __ A[left] __ target:
            r_ left
        __ A[right] __ target:
            r_ right
        r_ -1
