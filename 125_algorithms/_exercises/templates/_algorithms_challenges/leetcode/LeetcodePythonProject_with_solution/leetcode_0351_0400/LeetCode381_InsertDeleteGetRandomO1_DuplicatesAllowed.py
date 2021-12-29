'''
Created on Apr 1, 2017

@author: MT
'''

class RandomizedCollection(object):
    ___ __init__(self):
        self.vals = []
        self.pos = {}
    
    ___ insert(self, val):
        self.vals.append(val)
        __ val in self.pos:
            self.pos[val].add(len(self.vals)-1)
            return False
        else:
            self.pos[val] = set([len(self.vals)-1])
            return True
    
    ___ remove(self, val):
        __ val in self.pos:
            lastVal = self.vals[-1]
            ind = self.pos[val].pop()
            self.vals[ind] = lastVal
            __ self.pos[lastVal]:
                self.pos[lastVal].add(ind)
                self.pos[lastVal].discard(len(self.vals)-1)
            self.vals.pop()
            __ not self.pos[val]:
                del self.pos[val]
            return True
        return False
    
    ___ getRandom(self):
        import random
        return random.choice(self.vals)
    