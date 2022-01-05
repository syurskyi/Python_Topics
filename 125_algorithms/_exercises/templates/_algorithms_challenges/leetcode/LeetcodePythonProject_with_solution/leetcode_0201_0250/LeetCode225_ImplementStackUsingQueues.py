'''
Created on Feb 22, 2017

@author: MT
'''

c_ Solution(o..):
    ___ - ):
        queue1    # list
        queue2    # list
    
    ___ push  x):
        __ empty
            queue1.a..(x)
        ____:
            __ queue1:
                queue2.a..(x)
                w.... queue1:
                    queue2.a..(queue1.pop(0))
            ____:
                queue1.a..(x)
                w.... queue2:
                    queue1.a..(queue2.pop(0))
    
    ___ pop
        __ queue1:
            r.. queue1.pop(0)
        ____:
            r.. queue2.pop(0)
    
    ___ top
        __ queue1:
            r.. queue1[0]
        ____:
            r.. queue2[0]
    
    ___ empty
        r.. n.. queue1 a.. n.. queue2

__ _____ __ _____
    stack = Solution()
    stack.push(123)
    stack.push('a')
    print(stack.top())
    print(stack.pop())
    print(stack.top())
