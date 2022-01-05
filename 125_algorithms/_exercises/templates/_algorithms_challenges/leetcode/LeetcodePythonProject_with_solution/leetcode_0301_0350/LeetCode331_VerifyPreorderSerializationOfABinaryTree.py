'''
Created on Mar 19, 2017

@author: MT
'''

c_ Solution(o..):
    ___ isValidSerialization  preorder):
        __ n.. preorder: r.. F..
        nodes = preorder.s..(',')
        stack    # list
        ___ node __ nodes:
            stack.a..(node)
            w.... l..(stack)>=3 a.. stack[-1] __ '#' a.. stack[-2] __ '#' a..\
                stack[-3] != '#':
                stack.pop()
                stack.pop()
                stack.pop()
                stack.a..('#')
        r.. stack __ ['#']
