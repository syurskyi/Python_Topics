"""
Given a collection of numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].

"""


class Solution(object
    ___ permute(self, nums
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        __ not nums:
            r_ [[]]
        ____
            res = []
            ___ i, e in enumerate(nums
                rest = nums[:i] + nums[i + 1:]
                rest_perms = self.permute(rest)
                ___ perm in rest_perms:
                    perm.append(e)
                res += rest_perms
            r_ res
