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
        __ start >_ end:
            r.. A[end]

        left, right = start, end
        pivot = A[(start + end) // 2]

        w.... left <_ right:
            w.... left <_ right a.. A[left] < pivot:
                left += 1
            w.... left <_ right a.. A[right] > pivot:
                right -= 1

            __ left <_ right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1

        __ start <_ k <_ right:
            r.. quick_select(k, A, start, right)
        ____ left <_ k <_ end:
            r.. quick_select(k, A, left, end)
        ____
            r.. A[k]
