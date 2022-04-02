'''
Created on Apr 2, 2017

@author: MT
'''

c_ Solution(o..
    ___ - , nums
        nums = nums
    
    ___ reset
        r.. nums
    
    ___ shuffle
        _______ r__
        newNums = l..(nums)
        __ n.. newNums:
            r.. newNums
        ___ i __ r..(l..(newNums)-1, 0, -1
            ind = r__.randint(0, i)
            newNums[ind], newNums[i] = newNums[i], newNums[ind]
        r.. newNums
