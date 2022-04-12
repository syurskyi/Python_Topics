# -*- coding: utf-8 -*-
"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the
kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""
__author__ 'Daniel'
_______ h__


c_ Solution:
    ___ findKthLargest  nums, k
        """
        Algorithm:
        * Partial quick sort average O(n), worst case O(n^2)
        * Heap O(n lg k), kth largest element is the smallest one in the k-size heap.

        :rtype: int
        """
        h    # list
        n l..(nums)
        ___ i, v __ e..(nums
            __ i < k:
                h__.heappush(h, v)
            ____
                __ v <_ h[0]:
                    _____
                h__.heappop(h)
                h__.heappush(h, v)

        r.. h__.heappop(h)


__ _______ __ _______
    print Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2)

