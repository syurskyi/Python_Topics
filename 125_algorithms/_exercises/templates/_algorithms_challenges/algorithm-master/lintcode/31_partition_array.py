class Solution:
    """
    @param: A: The integer array you should partition
    @param: k: An integer
    @return: The index after partition
    """
    ___ partitionArray(self, A, k
        __ not A:
            r_ 0

        left, right = 0, le.(A) - 1

        w___ left <= right:
            w___ left <= right and A[left] < k:
                left += 1
            w___ left <= right and A[right] >= k:
                right -= 1

            __ left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1

        r_ left
