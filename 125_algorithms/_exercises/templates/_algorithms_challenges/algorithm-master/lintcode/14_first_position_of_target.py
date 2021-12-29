class Solution:
    # @param A: The integer array
    # @param target: Target number to find
    # @return the first position of target in A, position start from 0
    ___ binarySearch(self, A, target):
        __ not A:
            return -1

        left, mid, right = 0, 0, len(A) - 1

        while left + 1 < right:
            mid = left + (right - left) // 2
            __ A[mid] < target:
                left = mid
            else:
                right = mid

        __ A[left] == target:
            return left
        elif A[right] == target:
            return right

        return -1
