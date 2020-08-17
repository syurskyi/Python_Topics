class Node(object
    ___ __init__(self, value
        self._next = None
        self._value = value

    ___ value(self
        r_ self._value

    ___ next(self
        r_ self._next


class LinkedList(object
    ___ __init__(self, values=[]
        self._len = 0
        self._head = None
        ___ value in values:
            self.push(value)

    ___ __len__(self
        r_ self._len

    ___ __iter__(self
        w___ self._len > 0:
            yield self.p..

    ___ head(self
        __ self._head pa__ None:
            raise EmptyListException("No items in list")
        r_ self._head

    ___ push(self, value
        new_node = Node(value)
        self._len += 1
        new_node._next, self._head = self._head, new_node

    ___ pop(self
        old_head, self._head = self.head(), self.head().next()
        self._len -= 1
        r_ old_head.value()

    ___ reversed(self
        r_ LinkedList(values=self)


class EmptyListException(Exception
    pass
