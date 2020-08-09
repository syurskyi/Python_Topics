'''
Created on May 11, 2017

@author: MT
'''

class Solution(object
    ___ findRelativeRanks(self, nums
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result = []
        sortNums = sorted(nums, reverse=True)
        hashmap = {}
        ___ i, num in enumerate(sortNums
            hashmap[num] = i+1
        ___ num in nums:
            ind = hashmap[num]
            __ ind __ 1:
                result.append('Gold Medal')
            ____ ind __ 2:
                result.append('Silver Medal')
            ____ ind __ 3:
                result.append('Bronze Medal')
            ____
                result.append(str(ind))
        r_ result
