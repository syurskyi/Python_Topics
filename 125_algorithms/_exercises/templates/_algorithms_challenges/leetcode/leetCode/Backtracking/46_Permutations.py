#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    # Easy to understand: recursively.
    ___ permute  nums
        ans   # list
        self.dfs(nums, [], ans)
        r_ ans

    ___ dfs  nums, path, ans
        __ n.. nums:
            ans.a.. path)
        ___ i, n __ enumerate(nums
            self.dfs(nums[:i] + nums[i + 1:], path + [n], ans)


c.. Solution_2 o..
    # Pythonic way.  recursively.
    # According to: https://leetcode.com/discuss/42550/one-liners-in-python
    ___ permute  nums
        r_ [[n] + p
                ___ i, n __ enumerate(nums)
                ___ p __ self.permute(nums[:i] + nums[i + 1:])] or [[]]

"""
[]
[1]
[1,2,3]
"""
