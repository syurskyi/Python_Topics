class Solution:
    """
    @param: A: An integer array sorted in ascending order
    @param: target: An integer
    @return: An integer
    """
    ___ findPosition(self, A, target):
        __ not A:
            return -1

        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            __ A[mid] == target:
                return mid
            __ A[mid] < target:
                left = mid
            else:
                right = mid

        __ A[left] == target:
            return left
        __ A[right] == target:
            return right
        return -1
