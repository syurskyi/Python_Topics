c_ Solution:
    """
    @param: A: The integer array you should partition
    @param: k: An integer
    @return: The index after partition
    """
    ___ partitionArray  A, k
        __ n.. A:
            r.. 0

        left, right = 0, l..(A) - 1

        w.... left <= right:
            w.... left <= right a.. A[left] < k:
                left += 1
            w.... left <= right a.. A[right] >= k:
                right -= 1

            __ left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1

        r.. left
