____ lintcode _______ ListNode


class Stack:
    ___ __init__(self):
        self.dummy = self.tail = ListNode(-1)

    """
    @param: x: An integer
    @return: nothing
    """
    ___ push(self, x):
        node = ListNode(x)
        node.pre = self.tail
        self.tail.nxt = node
        self.tail = node

    """
    @return: nothing
    """
    ___ pop(self):
        __ self.isEmpty():
            r..
        node = self.tail
        self.tail = node.pre
        self.tail.nxt = node.pre = N..

    """
    @return: An integer
    """
    ___ top(self):
        __ self.isEmpty():
            r..
        r.. self.tail.val

    """
    @return: True if the stack is empty
    """
    ___ isEmpty(self):
        r.. self.dummy __ self.tail
