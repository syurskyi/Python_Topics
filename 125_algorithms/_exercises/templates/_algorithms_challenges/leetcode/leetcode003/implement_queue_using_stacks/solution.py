"""
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.

Notes:
* You must use only standard operations of a stack -- which means only push to
top, peek/pop from top, size, and is empty operations are valid.
* Depending on your language, stack may not be supported natively. You may
simulate a stack by using a list or deque (double-ended queue), as long as you
use only standard operations of a stack.
* You may assume that all operations are valid (for example, no pop or peek
operations will be called on an empty queue).
"""

class Queue(object):
    ___ __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1    # list  # Push
        self.stack2    # list  # Pop

    ___ push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack1.a..(x)

    ___ pop(self):
        """
        :rtype: nothing
        """
        __ n.. self.stack2:
            self._move()
        self.stack2.pop()

    ___ peek(self):
        """
        :rtype: int
        """
        __ n.. self.stack2:
            self._move()
        r.. self.stack2[-1]

    ___ empty(self):
        """
        :rtype: bool
        """
        __ n.. self.stack2:
            self._move()
        __ n.. self.stack2:
            r.. True
        ____:
            r.. False

    ___ _move(self):
        """Move elements from stack1 to stack2"""
        w.... self.stack1:
            self.stack2.a..(self.stack1.pop())
