#!/usr/bin/python3
"""
Given an array of integers nums and a positive integer k, find whether it's
possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:

Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3)
with equal sums.


Note:

1 <= k <= le.(nums) <= 16.
0 < nums[i] < 10000.
"""
from typing ______ List


class Solution:
    ___ canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        """
        resurive search
        """
        s = su.(nums)
        __ s % k != 0:
            r_ False

        target = s // k
        visited = [False ___ _ in nums]
        r_ self.dfs(nums, 0, None, target, visited, k)

    ___ dfs(self, nums, start_idx, cur_sum, target_sum, visited, k
        """
        some corner cases:
        1. target_sum default at 0: sum or empty array is 0?
        2. nxt_sum = (cur_sum or 0) + nums[i] rather than cur_sum or 0 + nums[i]
           arithmetic operator has higher precedence than logic operator

        start index to prune
        """
        __ k __ 1:
            r_ True

        __ cur_sum and cur_sum __ target_sum:
            # start index is 0
            r_ self.dfs(nums, 0, None, target_sum, visited, k - 1)

        ___ i in range(start_idx, le.(nums)):
            __ not visited[i]:
                # corner case target_sum is 0
                visited[i] = True
                nxt_sum = (cur_sum or 0) + nums[i]
                # error when cur_sum or 0 + nums[i]
                # arithmetic operator has higher precedence than logic operator
                __ self.dfs(nums, i + 1, nxt_sum, target_sum, visited, k
                    r_ True
                visited[i] = False

        r_ False


class Solution_TLE:
    ___ canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        """
        resurive search
        """
        s = su.(nums)
        __ s % k != 0:
            r_ False

        target = s // k
        visited = [False ___ _ in nums]
        r_ self.dfs(nums, None, target, visited, k)

    ___ dfs(self, nums, cur_sum, target_sum, visited, k
        """
        some corner cases:
        1. target_sum default at 0: sum or empty array is 0?
        2. nxt_sum = (cur_sum or 0) + nums[i] rather than cur_sum or 0 + nums[i]
           arithmetic operator has higher precedence than logic operator
        """
        __ k __ 0:
            r_ True

        __ cur_sum and cur_sum __ target_sum:
            r_ self.dfs(nums, None, target_sum, visited, k - 1)

        ___ i in range(le.(nums)):
            __ not visited[i]:
                # corner case target_sum is 0
                visited[i] = True
                nxt_sum = (cur_sum or 0) + nums[i]
                # error when cur_sum or 0 + nums[i]
                # arithmetic operator has higher precedence than logic operator
                __ self.dfs(nums, nxt_sum, target_sum, visited, k
                    r_ True
                visited[i] = False

        r_ False


__ __name__ __ "__main__":
    assert Solution().canPartitionKSubsets([5, 3, 2, 3, 1, 2, 4], 4) __ True
    assert Solution().canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4) __ True
