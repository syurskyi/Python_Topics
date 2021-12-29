'''
Created on Apr 1, 2017

@author: MT
'''

class RandomizedSet(object):
    ___ __init__(self):
        self.nums    # list
        self.pos = {}
    
    ___ insert(self, val):
        __ val n.. __ self.pos:
            self.nums.a..(val)
            self.pos[val] = l..(self.nums)-1
            r.. True
        ____:
            r.. False
    
    ___ remove(self, val):
        __ val __ self.pos:
            ind = self.pos[val]
            lastVal = self.nums[-1]
            self.nums[ind] = lastVal
            self.pos[lastVal] = ind
            del self.pos[val]
            self.nums.pop()
            r.. True
        r.. False
    
    ___ getRandom(self):
        _______ random
        r.. random.choice(self.nums)
