'''
Created on Apr 18, 2017

@author: MT
'''

c_ Solution(o..):
    ___ findDisappearedNumbers  nums):
        ___ num __ nums:
            ind = abs(num)-1
            __ nums[ind] > 0:
                nums[ind] = -nums[ind]
        res    # list
        ___ i, num __ e..(nums):
            __ num > 0:
                res.a..(i+1)
        r.. res
