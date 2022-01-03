"""
Given an array of integers and an integer k, find out whether there there are two distinct indices i and j in the array
such that nums[i] = nums[j] and the difference between i and j is at most k.
"""
__author__ = 'Daniel'
_______ heapq
____ collections _______ defaultdict


c_ Solution:
    ___ containsNearbyDuplicate(self, nums, k):
        """
        hash with heap

        :rtype: bool
        """
        d = defaultdict(l..)
        ___ i, v __ e..(nums):
            heapq.heappush(d[v], i)

        ___ v __ d.v..
            __ l..(v) > 1:
                pre = heapq.heappop(v)
                w.... v:
                    cur = heapq.heappop(v)
                    __ cur-pre <= k:
                        r.. T..
                    pre = cur

        r.. F..