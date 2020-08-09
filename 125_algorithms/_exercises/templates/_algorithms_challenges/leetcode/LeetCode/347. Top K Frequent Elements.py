"""
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:
You may assume k is always valid, 1 <= k <= number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
from collections ______ defaultdict
______ heapq

__author__ = 'Daniel'


class Counter(object
    ___ __init__(self, val, cnt
        self.val = val
        self.cnt = cnt

    ___ __cmp__(self, other
        r_ self.cnt - other.cnt


class Solution(object
    ___ topKFrequent(self, nums, K
        """
        Count and Maintain a heap with size k -> O(n lg k)
        Since python heapq does not support cmp, need to wrap data in a struct
        Need to use min heap instead of max heap, since we need to pop the minimal one
        :type nums: List[int]
        :type K: int
        :rtype: List[int]
        """
        cnt = defaultdict(int)
        ___ e in nums:
            cnt[e] += 1

        lst = []
        ___ k, v in cnt.items(
            lst.append(Counter(k, v))

        ret = []
        ___ elt in lst:
            __ le.(ret) < K:
                heapq.heappush(ret, elt)
            ____
                heapq.heappushpop(ret, elt)

        r_ map(lambda x: x.val, ret)

