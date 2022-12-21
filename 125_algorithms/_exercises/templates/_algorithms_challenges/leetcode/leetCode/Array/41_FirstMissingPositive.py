#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ firstMissingPositive  nums
        """
        :type nums: List[int]
        :rtype: int
        """
        # Put all i+1 in nums[i]
        nums_len = l..(nums)
        ___ i __ r..(nums_len
            # Swap nums[i] to the appropriate position until current
            # nums[i] can't be push to the list, which is <0 or >nums_len
            # By the way, pay attention to situation as [1,1].
            _____ nums[i] != i + 1 and 0 < nums[i] <= nums_len:
                index = nums[i] - 1
                __ nums[index] __ nums[i]:
                    break
                nums[i], nums[index] = nums[index], nums[i]
                # nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]

        ___ i __ r..(nums_len
            __ nums[i] != i + 1:
                r_ i + 1

        r_ nums_len + 1

"""
[]
[1,2,0]
[3,4,-1,1]
[3,4,-1,1,2,2,0,12,3]
"""
