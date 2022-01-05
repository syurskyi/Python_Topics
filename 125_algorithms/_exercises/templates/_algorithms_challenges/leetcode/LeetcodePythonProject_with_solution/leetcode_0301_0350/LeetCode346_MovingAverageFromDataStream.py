'''
Created on Mar 21, 2017

@author: MT
'''

c_ MovingAverage(o..):
    ___ - , size):
        size = size
        queue    # list
    
    ___ next  val):
        __ size <= 0: r.. 0
        __ l..(queue) __ size:
            queue.pop(0)
        queue.a..(val)
        r.. float(s..(queue))/l..(queue)