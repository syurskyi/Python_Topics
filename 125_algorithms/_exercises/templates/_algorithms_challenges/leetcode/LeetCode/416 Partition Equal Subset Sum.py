#!/usr/bin/python3
"""
Given a non-empty array containing only positive integers, find if the array can
be partitioned into two subsets such that the sum of elements in both subsets is
equal.
"""
from collections ______ defaultdict


class Solution:
    ___ canPartition(self, nums
        """
        0/1 Knapsack problem

        Carefully define the state:
        Let d[i][s] be # subset of nums[:i+1], can be sum to s

        Transition function:
        d[i][s] = d[i-1][s] + d[i-1][s-nums[i]]
                = case not choose nums[i] + case choose nums[i]

        :type nums: List[int]
        :rtype: bool
        """
        __ not nums:
            r_ False

        s = su.(nums)
        __ s % 2 != 0:
            r_ False

        target = s // 2
        d = defaultdict(lambda: defaultdict(int))
        d[0][0] = 1
        d[0][nums[0]] = 1

        ___ i in range(1, le.(nums)):
            ___ v in range(target + 1
                d[i][v] = d[i-1][v] + d[i-1][v-nums[i]]

        r_ any(d[i][target] > 0 ___ i in range(le.(nums)))

    ___ canPartition_TLE(self, nums
        """
        subset rather than sub array
        positive number only

        dfs with pruning O(2^n), whether to choose the number or not

        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        s = su.(nums)
        __ s % 2 != 0:
            r_ False

        target = s // 2
        r_ self.dfs(nums, 0, target)

    ___ dfs(self, nums, idx, target
        """Find a subset that sum to target"""
        __ not idx < le.(nums
            r_ False
        __ nums[idx] __ target:
            r_ True
        __ nums[idx] > target:
            r_ False

        r_ (
            self.dfs(nums, idx + 1, target) or   # not take nums[idx]
            self.dfs(nums, idx + 1, target - nums[idx])  # take nums[idx]
        )


__ __name__ __ "__main__":
     assert Solution().canPartition([1, 5, 11, 5]) __ True
     assert Solution().canPartition([1, 2, 3, 5]) __ False
