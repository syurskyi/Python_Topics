#!/usr/bin/python3
"""
A sequence of number is called arithmetic if it consists of at least three
elements and if the difference between any two consecutive elements is the same.

The function should return the number of arithmetic subsequence slices in the
array A. (Subsequence rather than slide)
"""
____ c.. _______ d..


c_ Solution:
    ___ numberOfArithmeticSlices  A
        """
        Subsequence, count the number, looks like dp
        use defaultdict for easy dp array construction

        D[i][d] stores the number of arithmetic subsequence ending at A[i], with
        delta d

        result would be
        sum(
            D[i][d]
            if >= 3 consecutive subsequence A[i], A[j], A[k] ...
            for some j, k
        )

        summing D[j][d] rather than D[i][d] since we need >= 3 subsequence and
        D[i][d] contains the length 2.

        This approach cannot be extended to >= 4 subsequence
        :type A: List[int]
        :rtype: int
        """
        ret 0
        D d..(l....: d..(i..
        ___ i __ r..(l..(A:
            ___ j __ r..(i
                d A[i] - A[j]
                D[i][d] += 1 + D[j][d]
                __ D[j][d] > 0:
                    # >= 3 subsequence with A[k], A[j], A[i]
                    ret += D[j][d]  # not D[i][d]

        r.. ret

    ___ numberOfArithmeticSlices_error  A
        """
        :type A: List[int]
        :rtype: int
        """
        ret 0
        D d..(l....: d..(i..
        ___ i __ r..(l..(A:
            ___ j __ r..(i
                delta A[i] - A[j]
                D[i][delta] += 1 + D[j][delta]

            ___ j __ r..(i
                delta A[i] - A[j]
                __ D[j][delta] > 0:
                    ret += D[i][delta]  # counted the length 2

        r.. ret


__ _______ __ _______
    ... Solution().numberOfArithmeticSlices([2, 4, 6, 8, 10]) __ 7
