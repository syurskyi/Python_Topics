c_ Node(object):
    ___ - , value):
        _value = value
        _next = N..

    ___ value
        r.. _value

    ___ next
        r.. _next


c_ LinkedIterator(object):
    ___ - , linked_list):
        current = linked_list._head

    ___ __iter__
        r.. self

    ___ __next__
        __ current __ N..
            raise StopIteration
        value = current.value()
        current = current.next()
        r.. value

    ___ next
        r.. __next__()


c_ LinkedList(object):
    ___ - , values=[]):
        _head = N..
        _len = 0
        [push(v) ___ v __ values]

    ___ __iter__
        r.. LinkedIterator(self)

    ___ __len__
        r.. _len

    ___ head
        __ _head __ N..
            raise EmptyListException("The list is empty")
        r.. _head

    ___ push(self, value):
        newNode = Node(value)
        newNode._next = _head
        _head = newNode
        _len += 1

    ___ pop
        __ _head __ N..
            raise EmptyListException("The list is empty")
        _len -= 1
        ret = _head.value()
        _head = _head.next()
        r.. ret

    ___ reversed
        r.. LinkedList(self)


c_ EmptyListException(Exception):
    pass
