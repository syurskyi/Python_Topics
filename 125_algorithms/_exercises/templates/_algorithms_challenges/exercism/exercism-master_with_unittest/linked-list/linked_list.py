class Node(object):
    ___ __init__(self, value, succeeding=N.., previous_ N..
        self.value = value
        self.succeeding = succeeding
        self.previous = previous


class LinkedList(object):

    ___ __init__(self):
        self.head = N..
        self.tail = N..
        self.length = 0

    ___ push(self, value):
        new_node = Node(value)
        self.length += 1
        __ self.tail __ n.. N..
            self.tail.succeeding = new_node
            new_node.previous = self.tail
        self.tail = new_node
        __ self.head __ N..
            self.head = new_node

    ___ pop(self):
        self.length -= 1
        __ self.tail __ n.. N..
            popped_node = self.tail
            self.tail = popped_node.previous
            r.. popped_node.value

    ___ unshift(self, value):
        new_node = Node(value)
        self.length += 1
        __ self.head __ n.. N..
            self.head.previous = new_node
            new_node.succeeding = self.head
        self.head = new_node
        __ self.tail __ N..
            self.tail = new_node

    ___ shift(self):
        self.length -= 1
        __ self.head __ n.. N..
            shifted_node = self.head
            self.head = shifted_node.succeeding
            r.. shifted_node.value

    ___ __len__(self):
        r.. self.length
