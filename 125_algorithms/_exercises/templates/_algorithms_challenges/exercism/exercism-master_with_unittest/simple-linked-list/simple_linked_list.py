c_ Node:
    ___ - , value, next_node_ N..
        _value value
        _next_node next_node

    ___ value
        r.. _value

    ___ next
        r.. _next_node


c_ LinkedList:
    ___ - , values=   # list
        _size 0
        _head N..

        ___ value __ values:
            push(value)

    ___ -l
        r.. _size

    ___ head
        __ _head __ N..
            r.. EmptyListException("Head is empty")
        r.. _head

    ___ push  value
        new_node Node(value, _head)
        _head new_node
        _size += 1

    ___ pop
        current_head head()
        _head current_head.next()
        _size -_ 1
        r.. current_head.v..()

    ___ r..
        r.. LinkedList(self)

    ___ -i
        r.. LinkedListIterator(self)


c_ LinkedListIterator:
    ___ - , linked_list
        _current linked_list._head

    ___ -i
        r.. _

    ___ -n
        __ _current __ N..
            r.. S..
        current_value _current.v..()
        _current _current.next()
        r.. current_value


c_ EmptyListException(E..
    ___ - , message
        message message
