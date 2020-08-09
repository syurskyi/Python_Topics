'''
Created on Apr 18, 2017

@author: MT
'''

class Solution(object
    ___ findDisappearedNumbers(self, nums
        for num in nums:
            ind = abs(num)-1
            __ nums[ind] > 0:
                nums[ind] = -nums[ind]
        res = []
        for i, num in enumerate(nums
            __ num > 0:
                res.append(i+1)
        r_ res
