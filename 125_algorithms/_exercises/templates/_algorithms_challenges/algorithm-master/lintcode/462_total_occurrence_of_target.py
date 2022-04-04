c_ Solution:
    ___ totalOccurrence  A, target
        """
        :type A: List[int]
        :type target: int
        :rtype: int

        given A == [a, b, b, b, c]
                       s     e

        using binary searching to find `s` and `e`
        ans is `e - s + 1`

        * s: start, e: end, l: left, r: right
             [a, b, b, b, c]
        r1    l  r,s
        r2           e,l  r
        """
        __ n.. A:
            r.. 0

        n = l..(A)

        left, mid, right = 0, 0, n - 1
        w.... left + 1 < right:
            mid = left + (right - left) // 2
            __ A[mid] < target:
                left = mid
            ____
                right = mid

        start = left __ A[left] __ target ____ right

        __ A[start] != target:
            r.. 0

        left, mid, right = 0, 0, n - 1
        w.... left + 1 < right:
            mid = left + (right - left) // 2
            __ A[mid] <_ target:
                left = mid
            ____
                right = mid

        end = right __ A[right] __ target ____ left

        r.. end - start + 1
