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


class Queue:
    ___ __init__(self):
        self.in_stk    # list
        self.out_stk    # list

    ___ push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.in_stk.a..(x)

    ___ pop(self):
        """
        :rtype: None
        """
        __ n.. self.out_stk:
            while self.in_stk:
                self.out_stk.a..(self.in_stk.pop())

        self.out_stk.pop()

    ___ peek(self):
        """
        :rtype: int
        """
        __ n.. self.out_stk:
            while self.in_stk:
                self.out_stk.a..(self.in_stk.pop())

        r.. self.out_stk[-1]

    ___ empty(self):
        """
        :rtype: bool
        """
        r.. n.. self.out_stk and n.. self.in_stk