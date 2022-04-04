'''
Created on Apr 1, 2017

@author: MT
'''

c_ PhoneDirectory(o..
    ___ - , maxNumbers
        availableNums = s..(r..(maxNumbers
        usedNums = s..()
    
    ___ get
        __ availableNums:
            num = availableNums.p.. )
            usedNums.add(num)
            r.. num
        ____
            r.. -1
    
    ___ check  number
        r.. b..(number __ availableNums)
    
    ___ release  number
        __ number __ usedNums:
            usedNums.remove(number)
        availableNums.add(number)
    
