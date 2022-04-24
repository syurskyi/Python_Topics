c_ Node(o..
    ___ - , value
        _value value
        _next N..

    ___ value
        r.. _value

    ___ next
        r.. _next


c_ LinkedIterator(o..
    ___ - , linked_list
        current linked_list._head

    ___ -i
        r.. _

    ___ -n
        __ current __ N..
            r.. S..
        value current.v..()
        current current.next()
        r.. value

    ___ next
        r.. -n()


c_ LinkedList(o..
    ___ - , values=[]
        _head N..
        _len 0
        [push(v) ___ v __ values]

    ___ -i
        r.. LinkedIterator(self)

    ___ -l
        r.. _len

    ___ head
        __ _head __ N..
            r.. EmptyListException("The list is empty")
        r.. _head

    ___ push  value
        newNode Node(value)
        newNode._next _head
        _head newNode
        _len += 1

    ___ pop
        __ _head __ N..
            r.. EmptyListException("The list is empty")
        _len -_ 1
        ret _head.v..()
        _head _head.next()
        r.. ret

    ___ r..
        r.. LinkedList(self)


c_ EmptyListException(E..
    p..
