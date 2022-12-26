#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ longestConsecutive  nums
        """
        Build a hash to find whether a num in nums or not in O(1) time.
        """
        nums_dict = {num: F.. ___ num __ nums}
        max_length = 0
        ___ num __ nums:
            __ nums_dict[num]:
                c_

            # Find the post consecutive number
            next_num = num + 1
            _____ next_num __ nums_dict:
                nums_dict[next_num] = True
                next_num += 1

            # Find the pre consecutive number
            pre_num = num - 1
            _____ pre_num __ nums_dict:
                nums_dict[pre_num] = True
                pre_num -= 1

            max_length = m..(next_num-pre_num-1, max_length)

        r_ max_length

"""
[]
[0]
[100, 4, 200, 1, 3, 2]
[2147483646,-2147483647,0,2,2147483644,-2147483645,2147483645]
"""
