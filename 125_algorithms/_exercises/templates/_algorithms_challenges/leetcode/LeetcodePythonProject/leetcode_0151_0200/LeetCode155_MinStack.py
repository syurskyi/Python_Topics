'''
Created on Feb 11, 2017

@author: MT
'''

class MinStack(object

    ___ __init__(self
        """
        initialize your data structure here.
        """
        self.stack = []

    ___ push(self, x
        """
        :type x: int
        :rtype: void
        """
        __ not self.stack:
            self.stack.append((x, x))
        ____
            self.stack.append((x, min(self.stack[-1][1], x)))

    ___ pop(self
        """
        :rtype: void
        """
        self.stack.pop()

    ___ top(self
        """
        :rtype: int
        """
        r_ self.stack[-1][0]

    ___ getMin(self
        """
        :rtype: int
        """
        r_ self.stack[-1][1]
