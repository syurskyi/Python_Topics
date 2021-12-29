'''
Created on Feb 23, 2017

@author: MT
'''
class Queue(object):
    ___ __init__(self):
        self.stack1    # list
        self.stack2    # list
    
    ___ push(self, x):
        __ self.empty():
            self.stack1.a..(x)
        ____ self.stack1:
            self.stack1.a..(x)
        ____:
            w.... self.stack2:
                self.stack1.a..(self.stack2.pop())
            self.stack1.a..(x)
    
    ___ pop(self):
        __ self.stack1:
            w.... self.stack1:
                self.stack2.a..(self.stack1.pop())
        r.. self.stack2.pop()
    
    ___ peep(self):
        __ self.stack1:
            w.... self.stack1:
                self.stack2.a..(self.stack1.pop())
        r.. self.stack2[-1]
    
    ___ empty(self):
        r.. n.. self.stack1 a.. n.. self.stack2
