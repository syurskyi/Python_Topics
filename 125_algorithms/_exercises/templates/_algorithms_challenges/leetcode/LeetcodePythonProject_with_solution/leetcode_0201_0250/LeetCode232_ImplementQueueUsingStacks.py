'''
Created on Feb 23, 2017

@author: MT
'''
class Queue(object):
    ___ __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    ___ push(self, x):
        __ self.empty():
            self.stack1.append(x)
        elif self.stack1:
            self.stack1.append(x)
        else:
            while self.stack2:
                self.stack1.append(self.stack2.pop())
            self.stack1.append(x)
    
    ___ pop(self):
        __ self.stack1:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
    
    ___ peep(self):
        __ self.stack1:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]
    
    ___ empty(self):
        return not self.stack1 and not self.stack2
