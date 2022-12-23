#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# @Last Modified time: 2016-07-01 21:00:38


c.. Solution o..
    ___ intersection  nums1, nums2
        r_ list(s..(nums1) & s..(nums2))


c.. Solution_2 o..
    ___ intersection  nums1, nums2
        ans   # list
        nums1_dict _ # dict
        ___ n __ nums1:
            nums1_dict[n] = nums1_dict.get(n, 0) + 1

        ___ n __ nums2:
            __ n __ nums1_dict a.. nums1_dict[n] != -1:
                ans.a.. n)
                nums1_dict[n] = -1
        r_ ans


c.. Solution_3 o..
    ___ intersection  nums1, nums2
        # sort the two list, and use two pointer to search to find common elements.
        ans   # list
        nums1.s.. )
        nums2.s.. )
        i = j = 0
        _____ (i < l..(nums1) a.. j < l..(nums2)):
            __ nums1[i] > nums2[j]:
                j += 1
            ____ nums1[i] < nums2[j]:
                i += 1
            ____
                __ n.. l..(ans) or nums1[i] != ans[-1]:
                    ans.a.. nums1[i])
                i += 1
                j += 1

        r_ ans

"""
[]
[]
[-1]
[]
[1,2,2,2,10,5]
[1,3,4,5,9]
"""
