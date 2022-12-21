#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ threeSum  nums
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        solution   # list
        nums.sort()
        length = l..(nums)
        ___ i __ r..(length-2
            # avoid duplicate triplets.
            __ i __ 0 or nums[i] > nums[i-1]:
                cur_num = nums[i]

                # Keep two points to scan double direction.
                left = i + 1
                right = length - 1
                _____ left < right:
                    __ nums[left] + nums[right] + cur_num < 0:
                        left += 1
                    ____ nums[left] + nums[right] + cur_num > 0:
                        right -= 1
                    ____
                        triplet = [cur_num, nums[left], nums[right]]
                        solution.append(triplet)
                        left += 1
                        right -= 1
                        # avoid duplicate triplets.
                        _____ left < right a.. nums[left] __ nums[left-1]:
                            left += 1
                        _____ left < right a.. nums[right] __ nums[right+1]:
                            right -= 1

        r_ solution

"""
[]
[-1,1,2,-1,-1,0,-2,1,1,3]
"""
