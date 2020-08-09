'''
Created on Mar 19, 2017

@author: MT
'''

class Solution(object
    ___ isValidSerialization(self, preorder
        __ not preorder: r_ False
        nodes = preorder.split(',')
        stack = []
        ___ node in nodes:
            stack.append(node)
            w___ le.(stack)>=3 and stack[-1] __ '#' and stack[-2] __ '#' and\
                stack[-3] != '#':
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append('#')
        r_ stack __ ['#']
