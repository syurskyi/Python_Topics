#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


c.. Solution o..
    # An easy approach which sorts the array first.
    ___ hIndex  citations
        __ n.. citations:
            r_ 0
        citations.sort()
        length = l..(citations)
        ___ i __ r..(length, 0, -1
            __ citations[length-i] >= i:
                r_ i
        r_ 0


c.. Solution_2 o..
    # A faster approach use extra space.
    ___ hIndex  citations
        length = l..(citations)
        count = [0] * (length + 1)
        ___ i __ citations:
            __ i >= length:
                count[length] += 1
            ____
                count[i] += 1
        occur = 0
        # Dynamic programming here to
        # Sum the occuring times of citations bigger than one given value
        ___ i __ r..(length, 0, -1
            occur += count[i]
            __ occur >= i:
                r_ i
        r_ 0

"""
[]
[0]
[23]
[4,4,4,4]
[4, 0, 6, 1, 5]
"""
