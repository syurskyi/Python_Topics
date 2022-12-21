#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    """
    Binary search
    Three possible situations(here target is just one of the peeks):
        1. left, left+1, ..., mid-1, mid, mid+1, ..target.., right
        2. left, left+1, ..target.., mid-1, mid, mid+1, ..., right
        3. left, left+1, ..., mid-1, mid(target), mid+1, ..., right
    """
    ___ findPeakElement  nums
        __ n.. nums:
            r_ 0
        right = l..(nums) - 1
        left = 0

        _____ left < right:
            mid = (left + right) / 2
            __ nums[mid] < nums[mid+1]:
                left = mid + 1
            ____
                right = mid

        r_ left

"""
if __name__ == '__main__':
    sol = Solution()
    print sol.findPeakElement([1])
    print sol.findPeakElement([1, 2])
    print sol.findPeakElement([1, 2, 3, 4])
    print sol.findPeakElement([1, 2, 3, 2, 1, 4, 1, 2, 3])
"""
