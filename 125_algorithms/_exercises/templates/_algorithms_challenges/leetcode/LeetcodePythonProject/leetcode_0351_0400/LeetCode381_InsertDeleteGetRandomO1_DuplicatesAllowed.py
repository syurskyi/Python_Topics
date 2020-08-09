'''
Created on Apr 1, 2017

@author: MT
'''

class RandomizedCollection(object
    ___ __init__(self
        self.vals = []
        self.pos = {}
    
    ___ insert(self, val
        self.vals.append(val)
        __ val in self.pos:
            self.pos[val].add(le.(self.vals)-1)
            r_ False
        ____
            self.pos[val] = set([le.(self.vals)-1])
            r_ True
    
    ___ remove(self, val
        __ val in self.pos:
            lastVal = self.vals[-1]
            ind = self.pos[val].pop()
            self.vals[ind] = lastVal
            __ self.pos[lastVal]:
                self.pos[lastVal].add(ind)
                self.pos[lastVal].discard(le.(self.vals)-1)
            self.vals.pop()
            __ not self.pos[val]:
                del self.pos[val]
            r_ True
        r_ False
    
    ___ getRandom(self
        ______ random
        r_ random.choice(self.vals)
    