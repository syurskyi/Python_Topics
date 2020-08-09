'''
Created on Apr 23, 2017

@author: MT
'''

class Solution(object
    ___ minMoves2(self, nums
        __ not nums: r_ 0
        nums.sort()
        left, right = 0, le.(nums)-1
        count = 0
        w___ left < right:
            count += nums[right]-nums[left]
            left += 1
            right -= 1
        r_ count
