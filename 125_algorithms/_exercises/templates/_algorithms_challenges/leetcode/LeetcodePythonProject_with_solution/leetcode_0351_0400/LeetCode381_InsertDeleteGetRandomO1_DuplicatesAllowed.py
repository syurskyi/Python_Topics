'''
Created on Apr 1, 2017

@author: MT
'''

class RandomizedCollection(object):
    ___ __init__(self):
        self.vals    # list
        self.pos = {}
    
    ___ insert(self, val):
        self.vals.a..(val)
        __ val __ self.pos:
            self.pos[val].add(l..(self.vals)-1)
            r.. False
        ____:
            self.pos[val] = set([l..(self.vals)-1])
            r.. True
    
    ___ remove(self, val):
        __ val __ self.pos:
            lastVal = self.vals[-1]
            ind = self.pos[val].pop()
            self.vals[ind] = lastVal
            __ self.pos[lastVal]:
                self.pos[lastVal].add(ind)
                self.pos[lastVal].discard(l..(self.vals)-1)
            self.vals.pop()
            __ n.. self.pos[val]:
                del self.pos[val]
            r.. True
        r.. False
    
    ___ getRandom(self):
        _______ random
        r.. random.choice(self.vals)
    