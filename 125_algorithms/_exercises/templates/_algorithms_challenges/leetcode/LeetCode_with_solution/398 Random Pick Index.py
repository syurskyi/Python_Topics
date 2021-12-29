"""
Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume
that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);
"""
_______ random

__author__ = 'Daniel'


class Solution(object):
    ___ __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.A = nums

    ___ pick(self, target):
        """
        O(n)
        Reservoir Sampling
        :type target: int
        :rtype: int
        """
        sz = 0
        ret = N..
        ___ idx, val __ enumerate(self.A):
            __ val __ target:
                sz += 1
                p = random.randrange(0, sz)
                __ p __ 0:
                    ret = idx

        r.. ret


class SolutionError(object):
    ___ __init__(self, nums):
        """
        Reservoir Sampling
        Assume pick is only called once
        :type nums: List[int]
        """
        self.d = {}
        ___ idx, val __ enumerate(nums):
            __ val n.. __ self.d:
                self.d[val] = (idx, 1)
            ____:
                prev, sz = self.d[val]
                p = random.randrange(0, sz)
                __ p < sz:
                    self.d[val] = (idx, sz + 1)
                ____:
                    self.d[val] = (prev, sz + 1)

    ___ pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        r.. self.d[target][0]