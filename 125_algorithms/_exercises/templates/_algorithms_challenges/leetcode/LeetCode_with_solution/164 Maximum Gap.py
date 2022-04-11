"""
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
"""
__author__ 'Daniel'
_______ ___


c_ Solution:
    ___ maximumGap  nums
        """
        Brute force O(n lgn)

        Data, gap -> distribution -> histogram
        Rough sort in bins in linear time

        :type nums: list[int]
        :rtype: int
        """
        n l..(nums)
        __ n < 2:
            r.. 0

        g_min m..(nums)
        g_max m..(nums)

        bin_width m..(1, (g_max-g_min)/n)
        bins_min    # dict
        bins_max    # dict
        ___ v __ nums:
            bin_id (v-g_min)/bin_width
            bins_min[bin_id] m..(bins_min.g.. bin_id, ___.maxint), v)
            bins_max[bin_id] m..(bins_max.g.. bin_id, -___.maxint-1), v)

        max_gap 0
        pre_max g_min
        ___ i __ x..(0, (g_max-g_min)/bin_width+1
            __ i __ bins_min:
                max_gap m..(max_gap, bins_min[i]-pre_max)
                pre_max bins_max[i]

        r.. max_gap

__ _______ __ _______
    ... Solution().maximumGap([1, 1000]) __ 999