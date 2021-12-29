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
        d = {}
        r.. self.permute(nums, d)

    ___ permute(self, nums, d):
        __ n.. nums:
            r.. [[]]
        ____:
            res    # list
            ___ i, c __ e..(nums):
                __ c __ d:
                    continue
                ____:
                    d[c] = True
                rest_perms = self.permuteUnique(nums[:i] + nums[i + 1:])
                ___ perm __ rest_perms:
                    perm.insert(0, c)
                res += rest_perms
            r.. res
