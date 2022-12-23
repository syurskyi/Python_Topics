#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# @Last Modified time: 2016-07-02 10:47:23


c.. Solution o..
    ___ intersect  nums1, nums2
        nums1_dict _ # dict
        ___ n __ nums1:
            nums1_dict[n] = nums1_dict.get(n, 0) + 1
        ans   # list
        ___ n __ nums2:
            __ nums1_dict.get(n, 0) > 0:
                ans.a.. n)
                nums1_dict[n] = nums1_dict.get(n, 0) - 1
        r_ ans


c.. Solution_2 o..
    ___ intersect  nums1, nums2
        nums1.s.. )
        nums2.s.. )
        i, j = 0, 0
        ans   # list
        _____ i < l..(nums1) a.. j < l..(nums2
            __ nums1[i] __ nums2[j]:
                ans.a.. nums1[i])
                i += 1
                j += 1
            ____ nums1[i] < nums2[j]:
                i += 1
            ____
                j += 1
        r_ ans

"""
[]
[]
[1,2,2,2,3]
[3,2,2,2,3]
[1, 2, 2, 1]
[2, 2]
"""
