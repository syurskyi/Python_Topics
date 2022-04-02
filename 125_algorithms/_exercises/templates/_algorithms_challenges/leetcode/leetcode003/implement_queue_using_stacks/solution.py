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

c_ Queue(o..
    ___ -
        """
        initialize your data structure here.
        """
        stack1    # list  # Push
        stack2    # list  # Pop

    ___ push  x
        """
        :type x: int
        :rtype: nothing
        """
        stack1.a..(x)

    ___ pop
        """
        :rtype: nothing
        """
        __ n.. stack2:
            _move()
        stack2.pop()

    ___ peek
        """
        :rtype: int
        """
        __ n.. stack2:
            _move()
        r.. stack2[-1]

    ___ empty
        """
        :rtype: bool
        """
        __ n.. stack2:
            _move()
        __ n.. stack2:
            r.. T..
        ____:
            r.. F..

    ___ _move
        """Move elements from stack1 to stack2"""
        w.... stack1:
            stack2.a..(stack1.pop
