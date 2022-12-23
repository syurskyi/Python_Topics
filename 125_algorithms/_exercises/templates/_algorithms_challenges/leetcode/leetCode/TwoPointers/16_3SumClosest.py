#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ threeSumClosest  nums, target
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.s.. )
        min_distance = 2 ** 31 - 1
        length = l..(nums)
        # keep the sum of three nums
        solution = 0
        ___ i __ r..(length-2
            cur_num = nums[i]
            left = i + 1
            right = length - 1
            _____ left < right:
                left_num = nums[left]
                right_num = nums[right]
                three_sum = cur_num + left_num + right_num

                # the right point go back
                __ three_sum > target:
                    right -= 1
                    __ min_distance > three_sum - target:
                        solution = three_sum
                        min_distance = three_sum - target
                # the left point go forward
                ____ three_sum < target:
                    __ min_distance > target - three_sum:
                        solution = three_sum
                        min_distance = target - three_sum
                    left += 1
                ____
                    r_ three_sum

        r_ solution

"""
[0,0,0]
1
[-1,-1,-1,-2,-3,1,2]
5
"""
