"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Stack Data Structure
"""
__author__ = 'Danyang'


c_ MinStack:
    ___ - 
        """
        algorithm: non_asc stack keeps the items of the normal stack if they are in non-ascending order
        normal stack: 5 4 3 5 4 3 2 1
        non-asc stack: 5 4 3 3 2 1

        when push: check whether in non-ascending order
        when pop: check whether in non-asc stack, if yes, pop it out from non-asc stack also

        if maintain the non_asc stack in this way, the non-ssc stack always keeps the non-ascending items of the normal
        stack
        :return:
        """
        stk    # list
        non_asc    # list

    ___ push  x
        """

        :param x: int
        :return: int
        """
        stk.a..(x)
        __ l..(non_asc) __ 0 o. x <= non_asc[-1]:  # rather than <
            non_asc.a..(x)

    ___ pop
        """

        :return: nothing
        """
        x = stk.pop()
        __ x __ non_asc[-1]:
            non_asc.pop()

    ___ top
        """

        :return: int
        """
        r.. stk[-1]

    ___ getMin
        """

        :return: int
        """
        r.. non_asc[-1]

