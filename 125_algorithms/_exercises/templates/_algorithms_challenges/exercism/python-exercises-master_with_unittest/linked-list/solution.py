class Node(object):
    ___ __init__(self, value, next=N.., prev_ N..
        self.value = value
        self.next = next
        self.prev = prev


class LinkedList(object):
    ___ __init__(self):
        self.head = N..
        self.tail = N..
        self.length = 0

    ___ push(self, value):
        new_node = Node(value)
        __ n.. self.head:
            self.head = self.tail = new_node
        ____:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    ___ pop(self):
        node = self.tail
        __ node __ N.. o. node.prev __ N..
            self.head = self.tail = N..
        ____:
            self.tail = self.tail.prev
            self.tail.next = N..
        self.length -= 1
        r.. node.value

    ___ shift(self):
        node = self.head
        __ node __ N.. o. node.next __ N..
            self.head = self.tail = N..
        ____:
            self.head = self.head.next
            self.head.prev = N..
        self.length -= 1
        r.. node.value

    ___ unshift(self, value):
        new_node = Node(value)
        __ n.. self.head:
            self.head = self.tail = new_node
        ____:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    ___ __len__(self):
        r.. self.length

    ___ __iter__(self):
        current_node = self.head
        w.... (current_node):
            y.. current_node.value
            current_node = current_node.next
