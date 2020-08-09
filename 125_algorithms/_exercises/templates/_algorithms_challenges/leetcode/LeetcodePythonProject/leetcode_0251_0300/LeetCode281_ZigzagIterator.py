'''
Created on Mar 6, 2017

@author: MT
'''

class ZigzagIterator(object
    ___ __init__(self, v1, v2
        self.vec = [v1, v2]
        self.pointer = 0
    
    ___ next(self
        w___ self.hashNext(
            __ self.vec[self.pointer]:
                val = self.vec[self.pointer][0]
                self.vec[self.pointer].pop()
                self.pointer += 1
                __ self.pointer >= le.(self.vec
                    self.pointer = 0
                r_ val
            ____
                self.pointer += 1
                __ self.pointer >= le.(self.vec
                    self.pointer = 0
        r_ None
    
    ___ hasNext(self
        r_ any([x != [] for x in self.vec])
