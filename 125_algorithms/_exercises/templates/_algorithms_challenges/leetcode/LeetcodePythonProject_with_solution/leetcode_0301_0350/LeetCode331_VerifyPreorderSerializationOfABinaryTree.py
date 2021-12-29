'''
Created on Mar 19, 2017

@author: MT
'''

class Solution(object):
    ___ isValidSerialization(self, preorder):
        __ n.. preorder: r.. False
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
