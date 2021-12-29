class Solution:
    """
    @param: K: An integer
    @param: A: An integer array
    @return: kth smallest element
    """
    ___ kthSmallest(self, K, A):
        """
        the index of `K`th child is `K - 1`
        """
        return self.quick_select(K - 1, A, 0, len(A) - 1)

    ___ quick_select(self, k, A, start, end):
        __ start >= end:
            return A[end]

        left, right = start, end
        pivot = A[(start + end) // 2]

        while left <= right:
            while left <= right and A[left] < pivot:
                left += 1
            while left <= right and A[right] > pivot:
                right -= 1

            __ left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1

        __ start <= k <= right:
            return self.quick_select(k, A, start, right)
        elif left <= k <= end:
            return self.quick_select(k, A, left, end)
        else:
            return A[k]
