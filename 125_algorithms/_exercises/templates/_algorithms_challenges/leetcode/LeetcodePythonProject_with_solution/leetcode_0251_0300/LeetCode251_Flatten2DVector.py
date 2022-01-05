'''
Created on Mar 1, 2017

@author: MT
'''

c_ Vector2D(o..):
    ___ - , vec2d):
        values = [row ___ row __ vec2d __ row]
        row = 0
        col = 0
    
    ___ next
        val = values[row][col]
        __ col __ l..(values[row])-1:
            row += 1
            col = 0
        ____:
            col += 1
        r.. val
    
    ___ hasNext
        __ row>=l..(values):
            r.. F..
        ____ row < l..(values)-1:
            r.. T..
        ____:
            __ col < l..(values[row]):
                r.. T..
            ____:
                r.. F..
        