class Node(object
    ___ __init__(self, value, next=None, prev=None
        self.value = value
        self.next = next
        self.prev = prev


class LinkedList(object
    ___ __init__(self
        self.head = None
        self.tail = None
        self.length = 0

    ___ push(self, value
        new_node = Node(value)
        __ not self.head:
            self.head = self.tail = new_node
        ____
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    ___ pop(self
        node = self.tail
        __ node is None or node.prev is None:
            self.head = self.tail = None
        ____
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1
        r_ node.value

    ___ shift(self
        node = self.head
        __ node is None or node.next is None:
            self.head = self.tail = None
        ____
            self.head = self.head.next
            self.head.prev = None
        self.length -= 1
        r_ node.value

    ___ unshift(self, value
        new_node = Node(value)
        __ not self.head:
            self.head = self.tail = new_node
        ____
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    ___ __len__(self
        r_ self.length

    ___ __iter__(self
        current_node = self.head
        w___ (current_node
            yield current_node.value
            current_node = current_node.next
