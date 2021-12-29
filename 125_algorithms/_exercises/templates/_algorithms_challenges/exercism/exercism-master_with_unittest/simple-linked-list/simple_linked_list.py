class Node:
    ___ __init__(self, value, next_node_ N..
        self._value = value
        self._next_node = next_node

    ___ value(self):
        r.. self._value

    ___ next(self):
        r.. self._next_node


class LinkedList:
    ___ __init__(self, values=[]):
        self._size = 0
        self._head = N..

        ___ value __ values:
            self.push(value)

    ___ __len__(self):
        r.. self._size

    ___ head(self):
        __ self._head __ N..
            raise EmptyListException("Head is empty")
        r.. self._head

    ___ push(self, value):
        new_node = Node(value, self._head)
        self._head = new_node
        self._size += 1

    ___ pop(self):
        current_head = self.head()
        self._head = current_head.next()
        self._size -= 1
        r.. current_head.value()

    ___ reversed(self):
        r.. LinkedList(self)

    ___ __iter__(self):
        r.. LinkedListIterator(self)


class LinkedListIterator:
    ___ __init__(self, linked_list):
        self._current = linked_list._head

    ___ __iter__(self):
        r.. self

    ___ __next__(self):
        __ self._current __ N..
            raise StopIteration
        current_value = self._current.value()
        self._current = self._current.next()
        r.. current_value


class EmptyListException(Exception):
    ___ __init__(self, message):
        self.message = message
