class Solution:
    """
    @param: A: an integer sorted array
    @param: target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    ___ searchRange(self, A, target
        NOT_FOUND = [-1, -1]

        __ not A:
            r_ NOT_FOUND

        n = le.(A)

        left, mid, right = 0, 0, n - 1
        w___ left + 1 < right:
            mid = left + (right - left) // 2
            __ A[mid] < target:
                left = mid
            ____
                right = mid

        start = left __ A[left] __ target else right

        left, mid, right = 0, 0, n - 1
        w___ left + 1 < right:
            mid = left + (right - left) // 2
            __ A[mid] <= target:
                left = mid
            ____
                right = mid

        end = right __ A[right] __ target else left

        __ start <= end:
            r_ [start, end]

        r_ NOT_FOUND
