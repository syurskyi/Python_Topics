#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    """
    Radix sort, you can see the explanation follow the links.
    https://www.cs.usfca.edu/~galles/visualization/RadixSort.html
    And here is a java solution in leetcode's discuss:
    https://leetcode.com/discuss/53636/radix-sort-solution-in-java-with-explanation
    """

    ___ maximumGap  nums
        __ n.. nums:
            r_ 0

        max_num = m..(nums)
        bucket = [[] ___ i __ r..(10)]
        exp = 1
        _____ max_num / exp > 0:
            ___ num __ nums:
                bucket[(num / exp) % 10].a.. num)
            nums   # list
            ___ each __ bucket:
                nums.e..(each)
            bucket = [[] ___ i __ r..(10)]
            exp *= 10

        max_gap = 0
        ___ i __ r..(1, l..(nums)):
            max_gap = m..(max_gap, nums[i] - nums[i - 1])
        r_ max_gap

"""
[]
[1]
[9,12,4,8,6,16,23]
[2,99999999]
"""
