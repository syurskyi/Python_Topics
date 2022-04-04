c_ Solution:
    """
    @param: K: An integer
    @param: A: An integer array
    @return: kth smallest element
    """
    ___ kthSmallest  K, A
        """
        the index of `K`th child is `K - 1`
        """
        r.. quick_select(K - 1, A, 0, l..(A) - 1)

    ___ quick_select  k, A, start, end
        __ start >= end:
            r.. A[end]

        left, right = start, end
        pivot = A[(start + end) // 2]

        w.... left <= right:
            w.... left <= right a.. A[left] < pivot:
                left += 1
            w.... left <= right a.. A[right] > pivot:
                right -= 1

            __ left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1

        __ start <= k <= right:
            r.. quick_select(k, A, start, right)
        ____ left <= k <= end:
            r.. quick_select(k, A, left, end)
        ____
            r.. A[k]
