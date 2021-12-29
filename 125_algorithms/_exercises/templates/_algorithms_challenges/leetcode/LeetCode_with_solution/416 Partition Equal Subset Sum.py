#!/usr/bin/python3
"""
Given a non-empty array containing only positive integers, find if the array can
be partitioned into two subsets such that the sum of elements in both subsets is
equal.
"""
____ collections _______ defaultdict


class Solution:
    ___ canPartition(self, nums):
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
        __ n.. nums:
            r.. False

        s = s..(nums)
        __ s % 2 != 0:
            r.. False

        target = s // 2
        d = defaultdict(l....: defaultdict(int))
        d[0][0] = 1
        d[0][nums[0]] = 1

        ___ i __ r..(1, l..(nums)):
            ___ v __ r..(target + 1):
                d[i][v] = d[i-1][v] + d[i-1][v-nums[i]]

        r.. any(d[i][target] > 0 ___ i __ r..(l..(nums)))

    ___ canPartition_TLE(self, nums):
        """
        subset rather than sub array
        positive number only

        dfs with pruning O(2^n), whether to choose the number or not

        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        s = s..(nums)
        __ s % 2 != 0:
            r.. False

        target = s // 2
        r.. self.dfs(nums, 0, target)

    ___ dfs(self, nums, idx, target):
        """Find a subset that sum to target"""
        __ n.. idx < l..(nums):
            r.. False
        __ nums[idx] __ target:
            r.. True
        __ nums[idx] > target:
            r.. False

        r.. (
            self.dfs(nums, idx + 1, target) o.   # not take nums[idx]
            self.dfs(nums, idx + 1, target - nums[idx])  # take nums[idx]
        )


__ __name__ __ "__main__":
     ... Solution().canPartition([1, 5, 11, 5]) __ True
     ... Solution().canPartition([1, 2, 3, 5]) __ False
