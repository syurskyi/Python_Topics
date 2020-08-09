'''
Created on Mar 1, 2017

@author: MT
'''

class Vector2D(object
    ___ __init__(self, vec2d
        self.values = [row ___ row in vec2d __ row]
        self.row = 0
        self.col = 0
    
    ___ next(self
        val = self.values[self.row][self.col]
        __ self.col __ le.(self.values[self.row])-1:
            self.row += 1
            self.col = 0
        ____
            self.col += 1
        r_ val
    
    ___ hasNext(self
        __ self.row>=le.(self.values
            r_ False
        ____ self.row < le.(self.values)-1:
            r_ True
        ____
            __ self.col < le.(self.values[self.row]
                r_ True
            ____
                r_ False
        