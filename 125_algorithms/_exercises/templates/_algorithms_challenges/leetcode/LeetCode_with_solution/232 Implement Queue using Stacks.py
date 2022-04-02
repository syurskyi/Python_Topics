"""
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Notes:
You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty
operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque
(double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
"""
__author__ = 'Daniel'


c_ Queue:
    ___ -
        in_stk    # list
        out_stk    # list

    ___ push  x
        """
        :type x: int
        :rtype: None
        """
        in_stk.a..(x)

    ___ pop
        """
        :rtype: None
        """
        __ n.. out_stk:
            w.... in_stk:
                out_stk.a..(in_stk.pop

        out_stk.pop()

    ___ peek
        """
        :rtype: int
        """
        __ n.. out_stk:
            w.... in_stk:
                out_stk.a..(in_stk.pop

        r.. out_stk[-1]

    ___ empty
        """
        :rtype: bool
        """
        r.. n.. out_stk a.. n.. in_stk