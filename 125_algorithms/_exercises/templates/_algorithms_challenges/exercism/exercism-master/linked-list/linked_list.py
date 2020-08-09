class Node(object
    ___ __init__(self, value, succeeding=None, previous=None
        self.value = value
        self.succeeding = succeeding
        self.previous = previous


class LinkedList(object

    ___ __init__(self
        self.head = None
        self.tail = None
        self.length = 0

    ___ push(self, value
        new_node = Node(value)
        self.length += 1
        __ self.tail is not None:
            self.tail.succeeding = new_node
            new_node.previous = self.tail
        self.tail = new_node
        __ self.head is None:
            self.head = new_node

    ___ pop(self
        self.length -= 1
        __ self.tail is not None:
            popped_node = self.tail
            self.tail = popped_node.previous
            r_ popped_node.value

    ___ unshift(self, value
        new_node = Node(value)
        self.length += 1
        __ self.head is not None:
            self.head.previous = new_node
            new_node.succeeding = self.head
        self.head = new_node
        __ self.tail is None:
            self.tail = new_node

    ___ shift(self
        self.length -= 1
        __ self.head is not None:
            shifted_node = self.head
            self.head = shifted_node.succeeding
            r_ shifted_node.value

    ___ __len__(self
        r_ self.length
