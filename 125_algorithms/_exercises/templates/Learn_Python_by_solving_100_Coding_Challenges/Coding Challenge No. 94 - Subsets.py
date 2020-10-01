# Subsets
# Question: Given a set of distinct integers, nums, return all possible subsets.
# Note: The solution set must not contain duplicate subsets.
# For example: If nums = [1,2,3], a solution is:
# [ [3], [1], [2], [1,2,3], [1,3], [2,3], [1,2], [] ].
# Solutions:


c_ Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    ___ subsets(, nums):
        __ nums is N..:
            r_   # list
        result _   # list
        nums.sort()
        dfs(nums, 0,   # list, result)
        r_ result

    ___ dfs(, nums, pos, list_temp, ret):
        # append new object with []
        ret.ap..(  # list + list_temp)
        ___ i __ ra..(pos, le.(nums)):
            list_temp.ap..(nums[i])
            dfs(nums, i + 1, list_temp, ret)
            list_temp.p..()


Solution().subsets([1,2,3])