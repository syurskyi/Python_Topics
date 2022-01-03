c_ Node(object):
    ___ - , value, next=N.., prev_ N..
        value = value
        next = next
        prev = prev


c_ LinkedList(object):
    ___ - ):
        head = N..
        tail = N..
        length = 0

    ___ push(self, value):
        new_node = Node(value)
        __ n.. head:
            head = tail = new_node
        ____:
            new_node.prev = tail
            tail.next = new_node
            tail = new_node
        length += 1

    ___ pop
        node = tail
        __ node __ N.. o. node.prev __ N..
            head = tail = N..
        ____:
            tail = tail.prev
            tail.next = N..
        length -= 1
        r.. node.value

    ___ shift
        node = head
        __ node __ N.. o. node.next __ N..
            head = tail = N..
        ____:
            head = head.next
            head.prev = N..
        length -= 1
        r.. node.value

    ___ unshift(self, value):
        new_node = Node(value)
        __ n.. head:
            head = tail = new_node
        ____:
            new_node.next = head
            head.prev = new_node
            head = new_node
        length += 1

    ___ __len__
        r.. length

    ___ __iter__
        current_node = head
        w.... (current_node):
            y.. current_node.value
            current_node = current_node.next
