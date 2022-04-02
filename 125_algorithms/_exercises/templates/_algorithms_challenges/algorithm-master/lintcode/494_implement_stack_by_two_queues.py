____ lintcode _______ ListNode


c_ Stack:
    ___ -
        dummy = tail = ListNode(-1)

    """
    @param: x: An integer
    @return: nothing
    """
    ___ push  x
        node = ListNode(x)
        node.pre = tail
        tail.nxt = node
        tail = node

    """
    @return: nothing
    """
    ___ pop
        __ isEmpty
            r..
        node = tail
        tail = node.pre
        tail.nxt = node.pre = N..

    """
    @return: An integer
    """
    ___ top
        __ isEmpty
            r..
        r.. tail.val

    """
    @return: True if the stack is empty
    """
    ___ isEmpty
        r.. dummy __ tail
