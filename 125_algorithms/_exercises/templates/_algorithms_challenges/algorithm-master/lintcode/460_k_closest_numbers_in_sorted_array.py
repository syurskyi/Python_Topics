c_ Solution:
    """
    @param: A: an integer array
    @param: target: An integer
    @param: k: An integer
    @return: an integer array
    """
    ___ kClosestNumbers  A, target, k
        __ n.. A:
            r.. []

        n l..(A)

        """
        if `b` in `A`:
            [a, b, b, b, c]
                      l  r
        else:
            [a, c, d, e, f]
             l  r
        """
        left, mid, right 0, 0, n - 1
        w.... left + 1 < right:
            mid left + (right - left) // 2
            __ A[mid] <_ target:
                left mid
            ____
                right mid

        """
        # handle out of range
        if `left` less than `0`
            only append `A[right]`
        if `right` great than `n - 1`
            only append `A[left]`

        # handle closest
        append first if that `num` is more closer `target`
        """
        ans [0] * k
        ___ i __ r..(k
            __ left < 0:
                ans[i] A[right]
                right += 1
            ____ right >_ n:
                ans[i] A[left]
                left -_ 1
            ____ A[right] - target < target - A[left]:
                ans[i] A[right]
                right += 1
            ____
                ans[i] A[left]
                left -_ 1

        r.. ans
