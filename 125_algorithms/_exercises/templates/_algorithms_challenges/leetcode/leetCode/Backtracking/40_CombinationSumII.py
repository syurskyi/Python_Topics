#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    """ Classic backtracking problem.

    One key point: for one specified number,
    just scan the number larger than it to avoid duplicate combinations.
    Besides, the current path need to be reset after dfs call in general.
    Here we can just use `path + [num]` to avoid modifying path, so no need to reset.
    """

    ___ combinationSum2  candidates, target
        __ n.. candidates:
            r_ []
        candidates.s.. )
        ans   # list
        self.dfs_search(candidates, 0, target, [], ans)
        r_ ans

    ___ dfs_search  candidates, start, target, path, ans
        __ target __ 0:
            ans.a.. path)
        ___ i __ xrange(start, l..(candidates)):
            num = candidates[i]
            __ num > target:
                r_
            # Here skip the same `adjacent` element to avoid duplicated.
            __ i > start a.. candidates[i] __ candidates[i - 1]:
                c_
            self.dfs_search(candidates, i + 1,
                            target - num, path + [num], ans)

"""
[]
1
[2, 5, 1, 4, 9]
11
[10, 1, 2, 7, 6, 1, 5]
8
"""
