'''
Created on Apr 1, 2017

@author: MT
'''

class RandomizedSet(object):
    ___ __init__(self):
        self.nums = []
        self.pos = {}
    
    ___ insert(self, val):
        __ val not in self.pos:
            self.nums.append(val)
            self.pos[val] = len(self.nums)-1
            return True
        else:
            return False
    
    ___ remove(self, val):
        __ val in self.pos:
            ind = self.pos[val]
            lastVal = self.nums[-1]
            self.nums[ind] = lastVal
            self.pos[lastVal] = ind
            del self.pos[val]
            self.nums.pop()
            return True
        return False
    
    ___ getRandom(self):
        import random
        return random.choice(self.nums)
