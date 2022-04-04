"""
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Notes:
You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is
empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque
(double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
"""
__author__ = 'Daniel'


c_ Stack:
    ___ -
        """
        initialize your data structure here.
        One queue cannot mimic the stack, then you should use two queues.
        """
        q = [[], []]

    ___ push  x
        """
        :type x: int
        :rtype: nothing
        """
        t = 0
        __ n.. q[t]:
            t ^= 1

        q[t].a..(x)

    ___ pop
        """
        :rtype: nothing
        """
        t = 0
        __ n.. q[t]:
            t ^= 1

        w.... l..(q[t]) > 1:
            q[t^1].a..(q[t].p.. 0

        r.. q[t].p.. )

    ___ top
        """
        :rtype:  int
        """
        popped = p.. )
        t = 0
        __ n.. q[t]:
            t ^= 1

        q[t].a..(popped)
        r.. popped

    ___ empty
        """
        :rtype: bool
        """
        r.. n.. q[0] a.. n.. q[1]
