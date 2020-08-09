class Node(object
    ___ __init__(self, value
        self._value = value
        self._next = None

    ___ value(self
        r_ self._value

    ___ next(self
        r_ self._next


class LinkedIterator(object
    ___ __init__(self, linked_list
        self.current = linked_list._head

    ___ __iter__(self
        r_ self

    ___ __next__(self
        __ self.current is None:
            raise StopIteration
        value = self.current.value()
        self.current = self.current.next()
        r_ value

    ___ next(self
        r_ self.__next__()


class LinkedList(object
    ___ __init__(self, values=[]
        self._head = None
        self._len = 0
        [self.push(v) for v in values]

    ___ __iter__(self
        r_ LinkedIterator(self)

    ___ __len__(self
        r_ self._len

    ___ head(self
        __ self._head is None:
            raise EmptyListException("The list is empty")
        r_ self._head

    ___ push(self, value
        newNode = Node(value)
        newNode._next = self._head
        self._head = newNode
        self._len += 1

    ___ pop(self
        __ self._head is None:
            raise EmptyListException("The list is empty")
        self._len -= 1
        ret = self._head.value()
        self._head = self._head.next()
        r_ ret

    ___ reversed(self
        r_ LinkedList(self)


class EmptyListException(Exception
    pass
