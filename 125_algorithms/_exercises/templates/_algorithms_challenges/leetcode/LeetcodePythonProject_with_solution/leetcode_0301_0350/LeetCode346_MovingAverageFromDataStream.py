'''
Created on Mar 21, 2017

@author: MT
'''

class MovingAverage(object):
    ___ __init__(self, size):
        self.size = size
        self.queue = []
    
    ___ next(self, val):
        __ self.size <= 0: return 0
        __ len(self.queue) == self.size:
            self.queue.pop(0)
        self.queue.append(val)
        return float(sum(self.queue))/len(self.queue)