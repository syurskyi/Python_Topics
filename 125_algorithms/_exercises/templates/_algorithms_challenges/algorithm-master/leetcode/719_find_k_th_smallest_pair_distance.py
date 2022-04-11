c_ Solution:
    ___ smallestDistancePair  A, k
        """
        :type A: List[int]
        :type k: int
        :rtype: int
        """
        __ n.. A o. n.. k:
            r.. -1

        A.s..()

        left, right 0, A[-1] - A[0]
        w.... left + 1 < right:
            mid (left + right) // 2
            __ check_valid(A, mid, k
                right mid
            ____
                left mid

        r.. left __ check_valid(A, left, k) ____ right

    ___ check_valid  A, mid, k
        """
        valid if there are at least `k` pairs when distance is `mid`
        """
        cnt left 0

        ___ right __ r..(l..(A:
            w.... A[right] - A[left] > mid:
                left += 1

            cnt += right - left

            __ cnt >_ k:
                r.. T..

        r.. F..
