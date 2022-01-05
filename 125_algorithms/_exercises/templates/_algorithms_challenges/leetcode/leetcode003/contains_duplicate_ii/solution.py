"""
Given an array of integers and an integer k, find out whether there are two
distinct indices i and j in the array such that nums[i] = nums[j] and the
difference between i and j is at most k.
"""

c_ Solution(o..):
    ___ containsNearbyDuplicate  nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d    # dict
        ___ i, e __ e..(nums):
            __ e __ d:
                __ i - d[e] <= k:
                    r.. T..
            d[e] = i
        r.. F..


args1 = [[1, 0, 1, 1], 1]
s = Solution()
print(s.containsNearbyDuplicate(*args1))
