'''
Created on Mar 6, 2017

@author: MT
'''

c_ ZigzagIterator(object):
    ___ - , v1, v2):
        vec = [v1, v2]
        pointer = 0
    
    ___ next
        w.... hashNext
            __ vec[pointer]:
                val = vec[pointer][0]
                vec[pointer].pop()
                pointer += 1
                __ pointer >= l..(vec):
                    pointer = 0
                r.. val
            ____:
                pointer += 1
                __ pointer >= l..(vec):
                    pointer = 0
        r.. N..
    
    ___ hasNext
        r.. any([x !   # list ___ x __ self.vec])
