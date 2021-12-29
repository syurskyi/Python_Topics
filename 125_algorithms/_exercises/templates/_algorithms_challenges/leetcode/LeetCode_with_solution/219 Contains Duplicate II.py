"""
Given an array of integers and an integer k, find out whether there there are two distinct indices i and j in the array
such that nums[i] = nums[j] and the difference between i and j is at most k.
"""
__author__ = 'Daniel'
_______ heapq
____ collections _______ defaultdict


class Solution:
    ___ containsNearbyDuplicate(self, nums, k):
        """
        hash with heap

        :rtype: bool
        """
        d = defaultdict(l..)
        ___ i, v __ enumerate(nums):
            heapq.heappush(d[v], i)

        ___ v __ d.values():
            __ l..(v) > 1:
                pre = heapq.heappop(v)
                while v:
                    cur = heapq.heappop(v)
                    __ cur-pre <= k:
                        r.. True
                    pre = cur

        r.. False