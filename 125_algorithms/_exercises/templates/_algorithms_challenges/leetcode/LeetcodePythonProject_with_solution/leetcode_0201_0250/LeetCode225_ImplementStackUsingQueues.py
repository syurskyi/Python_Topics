'''
Created on Feb 22, 2017

@author: MT
'''

class Solution(object):
    ___ __init__(self):
        self.queue1    # list
        self.queue2    # list
    
    ___ push(self, x):
        __ self.empty():
            self.queue1.a..(x)
        ____:
            __ self.queue1:
                self.queue2.a..(x)
                w.... self.queue1:
                    self.queue2.a..(self.queue1.pop(0))
            ____:
                self.queue1.a..(x)
                w.... self.queue2:
                    self.queue1.a..(self.queue2.pop(0))
    
    ___ pop(self):
        __ self.queue1:
            r.. self.queue1.pop(0)
        ____:
            r.. self.queue2.pop(0)
    
    ___ top(self):
        __ self.queue1:
            r.. self.queue1[0]
        ____:
            r.. self.queue2[0]
    
    ___ empty(self):
        r.. n.. self.queue1 a.. n.. self.queue2

__ __name__ __ '__main__':
    stack = Solution()
    stack.push(123)
    stack.push('a')
    print(stack.top())
    print(stack.pop())
    print(stack.top())
