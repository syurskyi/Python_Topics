'''
Created on Mar 1, 2017

@author: MT
'''

class Vector2D(object):
    ___ __init__(self, vec2d):
        self.values = [row for row in vec2d __ row]
        self.row = 0
        self.col = 0
    
    ___ next(self):
        val = self.values[self.row][self.col]
        __ self.col == len(self.values[self.row])-1:
            self.row += 1
            self.col = 0
        else:
            self.col += 1
        return val
    
    ___ hasNext(self):
        __ self.row>=len(self.values):
            return False
        elif self.row < len(self.values)-1:
            return True
        else:
            __ self.col < len(self.values[self.row]):
                return True
            else:
                return False
        