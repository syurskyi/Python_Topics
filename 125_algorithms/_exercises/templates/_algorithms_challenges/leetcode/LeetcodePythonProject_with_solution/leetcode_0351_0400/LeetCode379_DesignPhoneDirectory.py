'''
Created on Apr 1, 2017

@author: MT
'''

class PhoneDirectory(object):
    ___ __init__(self, maxNumbers):
        self.availableNums = set(r..(maxNumbers))
        self.usedNums = set()
    
    ___ get(self):
        __ self.availableNums:
            num = self.availableNums.pop()
            self.usedNums.add(num)
            r.. num
        ____:
            r.. -1
    
    ___ check(self, number):
        r.. bool(number __ self.availableNums)
    
    ___ release(self, number):
        __ number __ self.usedNums:
            self.usedNums.remove(number)
        self.availableNums.add(number)
    
