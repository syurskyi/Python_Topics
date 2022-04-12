"""
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:
You may assume k is always valid, 1 <= k <= number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
____ c.. _______ d..
_______ h__

__author__ 'Daniel'


c_ C..(o..
    ___ - , val, cnt
        val val
        cnt cnt

    ___ __cmp__  other
        r.. cnt - other.cnt


c_ Solution(o..
    ___ topKFrequent  nums, K
        """
        Count and Maintain a heap with size k -> O(n lg k)
        Since python heapq does not support cmp, need to wrap data in a struct
        Need to use min heap instead of max heap, since we need to pop the minimal one
        :type nums: List[int]
        :type K: int
        :rtype: List[int]
        """
        cnt d..(i..)
        ___ e __ nums:
            cnt[e] += 1

        lst    # list
        ___ k, v __ cnt.i..:
            lst.a..(C..(k, v

        ret    # list
        ___ elt __ lst:
            __ l..(ret) < K:
                h__.heappush(ret, elt)
            ____
                h__.heappushpop(ret, elt)

        r.. map(l.... x: x.val, ret)

