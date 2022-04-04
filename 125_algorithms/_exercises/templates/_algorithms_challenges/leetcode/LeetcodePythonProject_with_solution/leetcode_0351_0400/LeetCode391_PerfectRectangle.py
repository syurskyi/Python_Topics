'''
Created on Apr 2, 2017

@author: MT
'''

c_ Solution(o..
    ___ isRectangleCover  rectangles
        __ n.. rectangles:
            r.. F..
        x1, x2, y1, y2 = f__('inf'), f__('-inf'), f__('inf'), f__('-inf')
        hashset = s..()
        area = 0
        ___ rect __ rectangles:
            x1 = m..(x1, rect[0])
            y1 = m..(y1, rect[1])
            x2 = m..(x2, rect[2])
            y2 = m..(y2, rect[3])
            
            area += (rect[2]-rect[0])*(rect[3]-rect[1])
            
            __ (rect[0], rect[1]) n.. __ hashset:
                hashset.add((rect[0], rect[1]
            ____
                hashset.discard((rect[0], rect[1]
            __ (rect[0], rect[3]) n.. __ hashset:
                hashset.add((rect[0], rect[3]
            ____
                hashset.discard((rect[0], rect[3]
            __ (rect[2], rect[3]) n.. __ hashset:
                hashset.add((rect[2], rect[3]
            ____
                hashset.discard((rect[2], rect[3]
            __ (rect[2], rect[1]) n.. __ hashset:
                hashset.add((rect[2], rect[1]
            ____
                hashset.discard((rect[2], rect[1]
        
        __ (x1, y1) n.. __ hashset o.\
            (x1, y2) n.. __ hashset o.\
            (x2, y1) n.. __ hashset o.\
            (x2, y2) n.. __ hashset o.\
            l..(hashset) != 4:
            r.. F..
        
        r.. area __ (x2-x1)*(y2-y1)
        
    