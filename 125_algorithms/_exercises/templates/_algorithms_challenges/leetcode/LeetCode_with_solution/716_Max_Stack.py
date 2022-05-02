c_ MaxStack o..

    ___ -(self):
        """
        initialize your data structure here.
        """
        stack =    # list
        max_stack =    # list

    ___ push  x):
        """
        :type x: int
        :rtype: void
        """
        stack.append(x)
        __ l.. max_stack) __ 0:
            max_stack.append(x)
            r_
        __ max_stack[-1] > x:
            max_stack.append(max_stack[-1])
        ____
            max_stack.append(x)

    ___ pop(self):
        """
        :rtype: int
        """
        __ l.. stack) != 0:
            max_stack.pop(-1)
            r_ stack.pop(-1)

    ___ top(self):
        """
        :rtype: int
        """
        r_ stack[-1]

    ___ peekMax(self):
        """
        :rtype: int
        """
        __ l.. max_stack) != 0:
            r_ max_stack[-1]

    ___ popMax(self):
        """
        :rtype: int
        """
        val = peekMax()
        buff =    # list
        w.. top() != val:
            buff.append(pop())
        pop()
        w.. l.. buff) != 0:
            push(buff.pop(-1))
        r_ val
