#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ removeDuplicates  nums
        """
        :type nums: List[int]
        :rtype: int
        """
        first_occ = 0
        nums_l = l..(nums)
        count = 0
        _____ first_occ < nums_l:
            # The last single number occurence only once.
            __ first_occ __ nums_l - 1:
                nums[count] = nums[first_occ]
                count += 1
                ______

            # Always keep the first occurence of a number
            first_num = nums[first_occ]
            second_num = nums[first_occ+1]
            # Move the number occurence only once to it's position
            __ first_num != second_num:
                nums[count] = first_num
                count += 1
                first_occ += 1
                c_

            # Move the number occur twice to their positions
            __ first_num __ second_num:
                nums[count] = first_num
                nums[count+1] = second_num
                next_occ = first_occ+2
                _____ next_occ < nums_l a.. nums[next_occ] __ second_num:
                    next_occ += 1
                count += 2
                first_occ = next_occ
        r_ count


"""
[]
[1,1,1,1,2,2,2,3,3,3,4,5,6,6,6,7]
"""
