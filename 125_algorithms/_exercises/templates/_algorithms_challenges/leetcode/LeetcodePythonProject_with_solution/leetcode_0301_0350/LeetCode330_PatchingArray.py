'''
Created on Mar 19, 2017

@author: MT
'''

class Solution(object):
    ___ minPatches(self, nums, n):
        miss = 1
        added, i = 0, 0
        while miss <= n:
            __ i < l..(nums) and miss >= nums[i]:
                miss += nums[i]
                i+=1
            ____:
                miss += miss
                added += 1
        r.. added
