#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


c.. Solution o..
    ___ combinationSum3  k, n
        self.combination   # list
        self._combination_sum(k, n, [])
        r_ self.combination

    ___ _combination_sum  k, n, nums
        __ n.. k:
            __ s..(nums) __ n:
                # self.combination.append(nums)
                # Warning: nums[:] get a new list.
                # If not, we will get self.combination = [[], [], ...] finally.
                self.combination.a.. nums[:])
            ____
                r_

        # Get the new num from start
        start = 1
        __ nums:
            start = nums[-1] + 1
        ___ i __ r..(start, 10
            cur_sum = s..(nums) + i
            __ cur_sum <= n:
                nums.a.. i)
                self._combination_sum(k - 1, n, nums)
                del nums[-1]    # Backtracking
            ____
                ______

"""
0
3
3
7
9
45
"""
