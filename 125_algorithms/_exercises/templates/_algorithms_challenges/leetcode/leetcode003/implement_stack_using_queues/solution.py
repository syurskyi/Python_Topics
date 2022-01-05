"""
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.

Notes:

You must use only standard operations of a queue -- which means only push to
back, peek/pop from front, size, and is empty operations are valid.

Depending on your language, queue may not be supported natively. You may
simulate a queue by using a list or deque (double-ended queue), as long as you
use only standard operations of a queue.

You may assume that all operations are valid (for example, no pop or top
operations will be called on an empty stack).
"""

c_ Stack(object):
    ___ - ):
        """
        initialize your data structure here.
        push(x)
        1. Enqueue x into queue1

        pop()
        1. queue2 is initially empty, queue1 stores old elements:
            queue2 = []
            queue1 = [a, b, c, x]
        2. Dequeue each elements except the last one from queue1 to queue2:
            queue2 = [a, b, c]
            queue1 = [x]
        3. Dequeue the last element of queue1, and store it as x:
            x = x
            queue2 = [a, b, c]
            queue1 = []
        4. Swap queue1 and queue2:
            x = x
            queue1 = [a, b, c]
            queue2 = []
        5. Return x
        """
        queue1    # list
        queue2    # list

    ___ push  x):
        """
        :type x: int
        :rtype: nothing
        """
        queue1.a..(x)

    ___ pop
        """
        :rtype: nothing
        """
        w.... l..(queue1) > 1:
            queue2.a..(queue1.pop(0))
        res = queue1.pop(0)
        queue1, queue2 = queue2, queue1
        r.. res

    ___ top
        """
        :rtype: int
        """
        r.. queue1[-1]

    ___ empty
        """
        :rtype: bool
        """
        r.. n.. queue1
