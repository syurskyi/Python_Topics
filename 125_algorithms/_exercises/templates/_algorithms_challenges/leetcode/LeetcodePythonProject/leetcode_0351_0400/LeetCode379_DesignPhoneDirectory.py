'''
Created on Apr 1, 2017

@author: MT
'''

class PhoneDirectory(object
    ___ __init__(self, maxNumbers
        self.availableNums = set(range(maxNumbers))
        self.usedNums = set()
    
    ___ get(self
        __ self.availableNums:
            num = self.availableNums.pop()
            self.usedNums.add(num)
            r_ num
        ____
            r_ -1
    
    ___ check(self, number
        r_ bool(number in self.availableNums)
    
    ___ release(self, number
        __ number in self.usedNums:
            self.usedNums.remove(number)
        self.availableNums.add(number)
    
