'''
Created on Mar 21, 2017

@author: MT
'''

class MovingAverage(object
    ___ __init__(self, size
        self.size = size
        self.queue = []
    
    ___ next(self, val
        __ self.size <= 0: r_ 0
        __ le.(self.queue) __ self.size:
            self.queue.pop(0)
        self.queue.append(val)
        r_ float(su.(self.queue))/le.(self.queue)