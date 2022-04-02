'''
Created on Feb 23, 2017

@author: MT
'''
c_ Queue(o..
    ___ -
        stack1    # list
        stack2    # list
    
    ___ push  x
        __ empty
            stack1.a..(x)
        ____ stack1:
            stack1.a..(x)
        ____:
            w.... stack2:
                stack1.a..(stack2.pop
            stack1.a..(x)
    
    ___ pop
        __ stack1:
            w.... stack1:
                stack2.a..(stack1.pop
        r.. stack2.pop()
    
    ___ peep
        __ stack1:
            w.... stack1:
                stack2.a..(stack1.pop
        r.. stack2[-1]
    
    ___ empty
        r.. n.. stack1 a.. n.. stack2
