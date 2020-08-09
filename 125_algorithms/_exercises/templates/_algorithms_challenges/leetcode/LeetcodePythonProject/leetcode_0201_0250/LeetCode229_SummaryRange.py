'''
Created on Feb 22, 2017

@author: MT
'''

class Solution(object
    ___ summaryRanges(self, nums
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result = []
        __ not nums: r_ result
        i = 0
        w___ i < le.(nums
            start = nums[i]
            w___ i+1 < le.(nums) and nums[i+1] __ nums[i]+1:
                i+=1
            end = nums[i]
            __ end __ start:
                result.append('%s' % (start))
            ____
                result.append('%s->%s' % (start, end))
            i += 1
        r_ result