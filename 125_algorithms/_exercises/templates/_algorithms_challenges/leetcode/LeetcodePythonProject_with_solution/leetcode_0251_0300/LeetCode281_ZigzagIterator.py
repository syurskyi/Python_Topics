'''
Created on Mar 6, 2017

@author: MT
'''

class ZigzagIterator(object):
    ___ __init__(self, v1, v2):
        self.vec = [v1, v2]
        self.pointer = 0
    
    ___ next(self):
        while self.hashNext():
            __ self.vec[self.pointer]:
                val = self.vec[self.pointer][0]
                self.vec[self.pointer].pop()
                self.pointer += 1
                __ self.pointer >= l..(self.vec):
                    self.pointer = 0
                r.. val
            ____:
                self.pointer += 1
                __ self.pointer >= l..(self.vec):
                    self.pointer = 0
        r.. N..
    
    ___ hasNext(self):
        r.. any([x !   # list ___ x __ self.vec])
