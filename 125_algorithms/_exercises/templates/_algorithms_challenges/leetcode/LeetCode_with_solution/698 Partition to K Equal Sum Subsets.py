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

1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.
"""
____ t___ _______ L..


c_ Solution:
    ___ canPartitionKSubsets  nums: L..[i..], k: i..) __ b..:
        """
        resurive search
        """
        s = s..(nums)
        __ s % k != 0:
            r.. F..

        target = s // k
        visited = [F.. ___ _ __ nums]
        r.. dfs(nums, 0, N.., target, visited, k)

    ___ dfs  nums, start_idx, cur_sum, target_sum, visited, k
        """
        some corner cases:
        1. target_sum default at 0: sum or empty array is 0?
        2. nxt_sum = (cur_sum or 0) + nums[i] rather than cur_sum or 0 + nums[i]
           arithmetic operator has higher precedence than logic operator

        start index to prune
        """
        __ k __ 1:
            r.. T..

        __ cur_sum a.. cur_sum __ target_sum:
            # start index is 0
            r.. dfs(nums, 0, N.., target_sum, visited, k - 1)

        ___ i __ r..(start_idx, l..(nums:
            __ n.. visited[i]:
                # corner case target_sum is 0
                visited[i] = T..
                nxt_sum = (cur_sum o. 0) + nums[i]
                # error when cur_sum or 0 + nums[i]
                # arithmetic operator has higher precedence than logic operator
                __ dfs(nums, i + 1, nxt_sum, target_sum, visited, k
                    r.. T..
                visited[i] = F..

        r.. F..


c_ Solution_TLE:
    ___ canPartitionKSubsets  nums: L..[i..], k: i..) __ b..:
        """
        resurive search
        """
        s = s..(nums)
        __ s % k != 0:
            r.. F..

        target = s // k
        visited = [F.. ___ _ __ nums]
        r.. dfs(nums, N.., target, visited, k)

    ___ dfs  nums, cur_sum, target_sum, visited, k
        """
        some corner cases:
        1. target_sum default at 0: sum or empty array is 0?
        2. nxt_sum = (cur_sum or 0) + nums[i] rather than cur_sum or 0 + nums[i]
           arithmetic operator has higher precedence than logic operator
        """
        __ k __ 0:
            r.. T..

        __ cur_sum a.. cur_sum __ target_sum:
            r.. dfs(nums, N.., target_sum, visited, k - 1)

        ___ i __ r..(l..(nums:
            __ n.. visited[i]:
                # corner case target_sum is 0
                visited[i] = T..
                nxt_sum = (cur_sum o. 0) + nums[i]
                # error when cur_sum or 0 + nums[i]
                # arithmetic operator has higher precedence than logic operator
                __ dfs(nums, nxt_sum, target_sum, visited, k
                    r.. T..
                visited[i] = F..

        r.. F..


__ _______ __ _______
    ... Solution().canPartitionKSubsets([5, 3, 2, 3, 1, 2, 4], 4) __ T..
    ... Solution().canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4) __ T..
