'''
Created on Apr 2, 2017

@author: MT
'''

class Solution(object
    ___ isRectangleCover(self, rectangles
        __ not rectangles:
            r_ False
        x1, x2, y1, y2 = float('inf'), float('-inf'), float('inf'), float('-inf')
        hashset = set()
        area = 0
        ___ rect __ rectangles:
            x1 = min(x1, rect[0])
            y1 = min(y1, rect[1])
            x2 = ma.(x2, rect[2])
            y2 = ma.(y2, rect[3])
            
            area += (rect[2]-rect[0])*(rect[3]-rect[1])
            
            __ (rect[0], rect[1]) not __ hashset:
                hashset.add((rect[0], rect[1]))
            ____
                hashset.discard((rect[0], rect[1]))
            __ (rect[0], rect[3]) not __ hashset:
                hashset.add((rect[0], rect[3]))
            ____
                hashset.discard((rect[0], rect[3]))
            __ (rect[2], rect[3]) not __ hashset:
                hashset.add((rect[2], rect[3]))
            ____
                hashset.discard((rect[2], rect[3]))
            __ (rect[2], rect[1]) not __ hashset:
                hashset.add((rect[2], rect[1]))
            ____
                hashset.discard((rect[2], rect[1]))
        
        __ (x1, y1) not __ hashset or\
            (x1, y2) not __ hashset or\
            (x2, y1) not __ hashset or\
            (x2, y2) not __ hashset or\
            le.(hashset) != 4:
            r_ False
        
        r_ area __ (x2-x1)*(y2-y1)
        
    