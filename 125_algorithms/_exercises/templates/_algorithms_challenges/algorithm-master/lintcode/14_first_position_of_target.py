class Solution:
    # @param A: The integer array
    # @param target: Target number to find
    # @return the first position of target in A, position start from 0
    ___ binarySearch(self, A, target
        __ not A:
            r_ -1

        left, mid, right = 0, 0, le.(A) - 1

        w___ left + 1 < right:
            mid = left + (right - left) // 2
            __ A[mid] < target:
                left = mid
            ____
                right = mid

        __ A[left] __ target:
            r_ left
        ____ A[right] __ target:
            r_ right

        r_ -1
