#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


c.. NumArray o..
    ___ __init__  nums
        length = l..(nums)
        # dp[i]: sum of nums[0] to nums[i]
        # To process dp[0] easily we add 1 to length
        self.dp = [0] * (length+1)
        ___ i, n __ enumerate(nums
            self.dp[i] = self.dp[i-1] + n

    ___ sumRange  i, j
        # sum of elements nums[i..j], inclusive.
        r_ self.dp[j] - self.dp[i-1]

# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)
