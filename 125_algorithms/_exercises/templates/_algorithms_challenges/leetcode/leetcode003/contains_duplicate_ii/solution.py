"""
Given an array of integers and an integer k, find out whether there are two
distinct indices i and j in the array such that nums[i] = nums[j] and the
difference between i and j is at most k.
"""

class Solution(object
    ___ containsNearbyDuplicate(self, nums, k
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        ___ i, e in enumerate(nums
            __ e in d:
                __ i - d[e] <= k:
                    r_ True
            d[e] = i
        r_ False


args1 = [[1, 0, 1, 1], 1]
s = Solution()
print(s.containsNearbyDuplicate(*args1))
