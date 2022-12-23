#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    """ Classic backtracking problem.

    One key point: for one specified number,
    just scan itself and numbers larger than it to avoid duplicate combinations.
    Besides, the current path need to be reset after dfs call in general.
    Here we can just use `path + [num]` to avoid modifying path, so no need to reset.
    Refer to:
    https://discuss.leetcode.com/topic/23142/python-dfs-solution
    """
    ___ combinationSum  candidates, target
        __ n.. candidates:
            r_ []

        ans   # list
        candidates.s.. )
        self.dfs_search(candidates, 0, target, [], ans)
        r_ ans

    ___ dfs_search  candidates, start, target, path, ans
        __ target __ 0:
            ans.a.. path)
        ____
            ___ i __ xrange(start, l..(candidates)):
                # Cannot find the suitable sets, just return.
                num = candidates[i]
                __ num > target:
                    r_
                self.dfs_search(candidates, i, target - num, path + [num], ans)

"""
[]
2
[2, 3, 6, 7]
7
[1, 2, 3, 4]
10
"""
