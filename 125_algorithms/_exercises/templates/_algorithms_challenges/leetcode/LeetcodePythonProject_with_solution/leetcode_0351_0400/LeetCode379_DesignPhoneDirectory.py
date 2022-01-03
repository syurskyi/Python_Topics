'''
Created on Apr 1, 2017

@author: MT
'''

c_ PhoneDirectory(object):
    ___ - , maxNumbers):
        availableNums = set(r..(maxNumbers))
        usedNums = set()
    
    ___ get
        __ availableNums:
            num = availableNums.pop()
            usedNums.add(num)
            r.. num
        ____:
            r.. -1
    
    ___ check(self, number):
        r.. bool(number __ availableNums)
    
    ___ release(self, number):
        __ number __ usedNums:
            usedNums.remove(number)
        availableNums.add(number)
    
