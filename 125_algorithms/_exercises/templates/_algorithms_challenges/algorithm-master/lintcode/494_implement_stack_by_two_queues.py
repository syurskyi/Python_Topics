from lintcode import ListNode


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
            return
        node = self.tail
        self.tail = node.pre
        self.tail.nxt = node.pre = None

    """
    @return: An integer
    """
    ___ top(self):
        __ self.isEmpty():
            return
        return self.tail.val

    """
    @return: True if the stack is empty
    """
    ___ isEmpty(self):
        return self.dummy is self.tail
