'''
Created on Mar 19, 2017

@author: MT
'''

class Solution(object):
    ___ isValidSerialization(self, preorder):
        __ n.. preorder: r.. False
        nodes = preorder.split(',')
        stack    # list
        ___ node __ nodes:
            stack.a..(node)
            while l..(stack)>=3 and stack[-1] __ '#' and stack[-2] __ '#' and\
                stack[-3] != '#':
                stack.pop()
                stack.pop()
                stack.pop()
                stack.a..('#')
        r.. stack __ ['#']
