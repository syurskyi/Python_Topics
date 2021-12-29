class Node(object):
    ___ __init__(self, value):
        self._value = value
        self._next = N..

    ___ value(self):
        r.. self._value

    ___ next(self):
        r.. self._next


class LinkedIterator(object):
    ___ __init__(self, linked_list):
        self.current = linked_list._head

    ___ __iter__(self):
        r.. self

    ___ __next__(self):
        __ self.current __ N..
            raise StopIteration
        value = self.current.value()
        self.current = self.current.next()
        r.. value

    ___ next(self):
        r.. self.__next__()


class LinkedList(object):
    ___ __init__(self, values=[]):
        self._head = N..
        self._len = 0
        [self.push(v) ___ v __ values]

    ___ __iter__(self):
        r.. LinkedIterator(self)

    ___ __len__(self):
        r.. self._len

    ___ head(self):
        __ self._head __ N..
            raise EmptyListException("The list is empty")
        r.. self._head

    ___ push(self, value):
        newNode = Node(value)
        newNode._next = self._head
        self._head = newNode
        self._len += 1

    ___ pop(self):
        __ self._head __ N..
            raise EmptyListException("The list is empty")
        self._len -= 1
        ret = self._head.value()
        self._head = self._head.next()
        r.. ret

    ___ reversed(self):
        r.. LinkedList(self)


class EmptyListException(Exception):
    pass
