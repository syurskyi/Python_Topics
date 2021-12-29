"""
Given a collection of numbers that might contain duplicates, return all
possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].
"""

class Solution(object):
    ___ permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.permute(sorted(nums))

    ___ permute(self, nums):
        __ not nums:
            return [[]]
        else:
            res = []
            prev = None
            for i, e in enumerate(nums):
                __ prev is None or prev != e:
                    rest = nums[:i] + nums[i + 1:]
                    rest_perms = self.permute(rest)
                    for perm in rest_perms:
                        perm.append(e)
                    res += rest_perms
                    prev = e
            return res
