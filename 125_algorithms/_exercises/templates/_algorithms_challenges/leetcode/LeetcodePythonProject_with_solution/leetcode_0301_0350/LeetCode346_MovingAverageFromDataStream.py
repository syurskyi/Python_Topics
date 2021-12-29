'''
Created on Mar 21, 2017

@author: MT
'''

class MovingAverage(object):
    ___ __init__(self, size):
        self.size = size
        self.queue    # list
    
    ___ next(self, val):
        __ self.size <= 0: r.. 0
        __ l..(self.queue) __ self.size:
            self.queue.pop(0)
        self.queue.a..(val)
        r.. float(s..(self.queue))/l..(self.queue)