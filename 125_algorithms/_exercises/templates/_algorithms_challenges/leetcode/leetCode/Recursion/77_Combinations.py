#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ combine  n, k
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        __ k > n or n.. n:
            r_ []

        combine_list = self.combine_k(1, n, k)
        r_ combine_list

    ___ combine_k  start, n, k
        combine_k   # list
        # k == 1, just return the list[start, end]
        __ k __ 1:
            ___ i __ r..(start, n+1
                combine_k.a.. [i])
            r_ combine_k

        # k > 1, return every i combines all the k-1 th combine in [i+1, n]
        ___ i __ r..(start, n+2-k
            combine_k_1 = self.combine_k(i+1, n, k-1)
            ___ combine_1 __ combine_k_1:
                combine = [i]
                combine.e..(combine_1)
                combine_k.a.. combine)

        r_ combine_k

"""
5
2
2
3
6
6
"""
