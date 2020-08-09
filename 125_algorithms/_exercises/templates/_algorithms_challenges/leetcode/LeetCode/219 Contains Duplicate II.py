"""
Given an array of integers and an integer k, find out whether there there are two distinct indices i and j in the array
such that nums[i] = nums[j] and the difference between i and j is at most k.
"""
__author__ = 'Daniel'
______ heapq
from collections ______ defaultdict


class Solution:
    ___ containsNearbyDuplicate(self, nums, k
        """
        hash with heap

        :rtype: bool
        """
        d = defaultdict(list)
        ___ i, v in enumerate(nums
            heapq.heappush(d[v], i)

        ___ v in d.values(
            __ le.(v) > 1:
                pre = heapq.heappop(v)
                w___ v:
                    cur = heapq.heappop(v)
                    __ cur-pre <= k:
                        r_ True
                    pre = cur

        r_ False