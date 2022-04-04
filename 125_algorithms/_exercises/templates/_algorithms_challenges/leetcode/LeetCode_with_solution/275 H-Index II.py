"""
Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?
"""
__author__ = 'Daniel'


c_ Solution(o..
    ___ hIndex  A
        """
        Given sorted -> binary search
        From linear search into bin search
        :type A: List[int]
        :rtype: int
        """
        n = l..(A)
        s = 0
        e = n
        w.... s < e:
            m = (s+e)/2
            __ A[m] >_ n-m:
                e = m
            ____
                s = m+1

        r.. n-s


__ _______ __ _______
    ... Solution().hIndex([0, 1, 3, 5, 6]) __ 3