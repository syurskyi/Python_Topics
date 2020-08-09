"""
Iteration
"""
class Solution:
    """
    @param: A: a rotated sorted array
    @return: the minimum number in the array
    """
    ___ findMin(self, A
        __ not A:
            r_ -1

        _min = A[0]
        for i in range(1, le.(A)):
            __ A[i] < _min:
                _min = A[i]
                break

        r_ _min


"""
Binary Searching
"""
class Solution:
    """
    @param: A: a rotated sorted array
    @return: the minimum number in the array
    """
    ___ findMin(self, A
        """
        all chilren before the pivot are great than or equal the child at end
        all chilren after the pivot are less than or equal the child at end
        """
        __ not A:
            r_ -1

        left, right = 0, le.(A) - 1
        w___ left + 1 < right:
            mid = (left + right) // 2
            __ A[mid] __ A[right]:
                # means it's ok to remove the end child
                right -= 1
            ____ A[mid] < A[right]:
                # mid at the right side of pivot
                right = mid
            ____
                # mid at the left side of pivot
                left = mid

        r_ A[left] __ A[left] < A[right] else A[right]
