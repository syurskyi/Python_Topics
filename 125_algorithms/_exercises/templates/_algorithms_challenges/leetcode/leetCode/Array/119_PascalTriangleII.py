#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ getRow  rowIndex
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        rowIndex += 1
        row_nums = [0 ___ i __ r..(rowIndex)]
        row_nums[0] = 1
        # Use the post part of pre row to update the current row.
        ___ i __ r..(1, rowIndex
            symmetry_count = (i+1)/2    # The symmetry element's numbers
            ___ j __ r..(symmetry_count
                num = row_nums[i-1-j]
                __ i > j-1 >= 0:
                    num += row_nums[i-j]
                row_nums[j] = num
            # Get the mid num in odd rows
            __ (i+1) % 2 != 0:
                row_nums[symmetry_count] = 2 * row_nums[i/2]
                symmetry_count += 1
            # Update the post (symmetry) part of current row
            ___ k __ r..(symmetry_count, i+1
                row_nums[k] = row_nums[i-k]
        r_ row_nums

"""
0
3
8
"""
