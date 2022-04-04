'''
Created on Feb 11, 2017

@author: MT
'''

c_ MinStack(o..

    ___ -
        """
        initialize your data structure here.
        """
        stack    # list

    ___ push  x
        """
        :type x: int
        :rtype: void
        """
        __ n.. stack:
            stack.a..((x, x
        ____:
            stack.a..((x, m..(stack[-1][1], x)))

    ___ pop
        """
        :rtype: void
        """
        stack.pop()

    ___ top
        """
        :rtype: int
        """
        r.. stack[-1][0]

    ___ getMin
        """
        :rtype: int
        """
        r.. stack[-1][1]
