'''
Created on May 11, 2017

@author: MT
'''

class Solution(object):
    ___ findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result    # list
        sortNums = s..(nums, r.._T..
        hashmap = {}
        ___ i, num __ enumerate(sortNums):
            hashmap[num] = i+1
        ___ num __ nums:
            ind = hashmap[num]
            __ ind __ 1:
                result.a..('Gold Medal')
            ____ ind __ 2:
                result.a..('Silver Medal')
            ____ ind __ 3:
                result.a..('Bronze Medal')
            ____:
                result.a..(str(ind))
        r.. result
