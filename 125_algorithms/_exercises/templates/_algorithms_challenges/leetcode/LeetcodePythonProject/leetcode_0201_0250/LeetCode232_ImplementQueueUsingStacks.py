'''
Created on Feb 23, 2017

@author: MT
'''
class Queue(object
    ___ __init__(self
        self.stack1 =   # list
        self.stack2 =   # list
    
    ___ push(self, x
        __ self.empty(
            self.stack1.append(x)
        ____ self.stack1:
            self.stack1.append(x)
        ____
            w___ self.stack2:
                self.stack1.append(self.stack2.pop())
            self.stack1.append(x)
    
    ___ pop(self
        __ self.stack1:
            w___ self.stack1:
                self.stack2.append(self.stack1.pop())
        r_ self.stack2.p..
    
    ___ peep(self
        __ self.stack1:
            w___ self.stack1:
                self.stack2.append(self.stack1.pop())
        r_ self.stack2[-1]
    
    ___ empty(self
        r_ not self.stack1 and not self.stack2
