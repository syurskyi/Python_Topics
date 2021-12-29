'''
Created on Mar 1, 2017

@author: MT
'''

class Vector2D(object):
    ___ __init__(self, vec2d):
        self.values = [row ___ row __ vec2d __ row]
        self.row = 0
        self.col = 0
    
    ___ next(self):
        val = self.values[self.row][self.col]
        __ self.col __ l..(self.values[self.row])-1:
            self.row += 1
            self.col = 0
        ____:
            self.col += 1
        r.. val
    
    ___ hasNext(self):
        __ self.row>=l..(self.values):
            r.. False
        ____ self.row < l..(self.values)-1:
            r.. True
        ____:
            __ self.col < l..(self.values[self.row]):
                r.. True
            ____:
                r.. False
        