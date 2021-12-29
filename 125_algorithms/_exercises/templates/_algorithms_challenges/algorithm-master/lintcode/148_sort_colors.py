class Solution:
    """
    @param: A: A list of integer which is 0, 1 or 2
    @return: nothing
    """
    ___ sortColors(self, A):
        __ not A:
            return

        left, right = 0, len(A) - 1
        i = 0
        while i <= right:
            __ A[i] == 0:
                A[left], A[i] = A[i], A[left]
                left += 1
                i += 1
            elif A[i] == 1:
                """
                temply ignore it
                it will be swapped if there is `0` later
                """
                i += 1
            else:
                """
                cannot `i += 1` since the swapped value still need to check
                """
                A[right], A[i] = A[i], A[right]
                right -= 1
