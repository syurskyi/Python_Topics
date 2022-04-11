c_ Solution:
    """
    @param: L: Given n pieces of wood with length L[i]
    @param: k: An integer
    @return: The maximum length of the small pieces
    """
    ___ woodCut  L, k
        """
        Assuming the `m` is the maximum length
        len   | ... m-2 m-1 m m+1 m+2 ...
        check |  T   T   T  T  F   F   F
        * check: is it ok to cut into at least `k` pieces
        """
        __ n.. L o. n.. k:
            r.. 0

        left 1
        total_len right L[0]
        ___ i __ r..(1, l..(L:
            __ L[i] > right:
                right L[i]

            total_len += L[i]

        __ total_len < k:
            r.. 0

        w.... left + 1 < right:
            mid (left + right) // 2
            __ check_if_possible(L, mid, k
                left mid
            ____
                right mid

        r.. right __ check_if_possible(L, right, k) ____ left

    ___ check_if_possible  L, size, max_pieces
        pieces 0

        ___ i __ r..(l..(L:
            pieces += L[i] // size
            __ pieces >_ max_pieces:
                r.. T..

        r.. F..
