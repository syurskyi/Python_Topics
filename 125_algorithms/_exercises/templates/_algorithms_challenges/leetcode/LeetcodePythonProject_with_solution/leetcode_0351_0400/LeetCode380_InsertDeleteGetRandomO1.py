'''
Created on Apr 1, 2017

@author: MT
'''

c_ RandomizedSet(object):
    ___ - ):
        nums    # list
        pos    # dict
    
    ___ insert(self, val):
        __ val n.. __ pos:
            nums.a..(val)
            pos[val] = l..(nums)-1
            r.. T..
        ____:
            r.. F..
    
    ___ remove(self, val):
        __ val __ pos:
            ind = pos[val]
            lastVal = nums[-1]
            nums[ind] = lastVal
            pos[lastVal] = ind
            del pos[val]
            nums.pop()
            r.. T..
        r.. F..
    
    ___ getRandom
        _______ r__
        r.. r__.choice(nums)
