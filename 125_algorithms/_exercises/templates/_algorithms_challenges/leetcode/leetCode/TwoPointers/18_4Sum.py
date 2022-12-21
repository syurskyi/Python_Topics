#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ fourSum  nums, target
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        solution   # list
        length = l..(nums)

        ___ i __ r..(length - 3
            # avoid duplicate triplets.
            __ i > 0 a.. nums[i] __ nums[i-1]:
                c_

            a = nums[i]
            ___ j __ r..(i + 1, length - 2
                # avoid duplicate triplets.
                __ j > i+1 a.. nums[j] __ nums[j-1]:
                    c_

                # Two points which are form head and bottom move toward
                # to make the a + b + c + d == target
                b = nums[j]
                left = j + 1
                right = length - 1
                _____ left < right:
                    c = nums[left]
                    d = nums[right]
                    __ a + b + c + d < target:
                        left += 1
                    ____ a + b + c + d > target:
                        right -= 1
                    ____
                        solution.append([a, b, c, d])
                        # avoid duplicate triplets.
                        left += 1
                        _____ left < right a.. nums[left] __ nums[left-1]:
                            left += 1
                        right -= 1
                        _____ right > left a.. nums[right] __ nums[right+1]:
                            right -= 1

        r_ solution

"""
[]
0
[1, 0, -1, 0, -2, 2]
0
[-2,-2,-2,-2,-1,-1,-1,-1,1,1,1,1,2,2,2,2,0,0,0]
0
"""
