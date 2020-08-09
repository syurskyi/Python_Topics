class Node(object
    ___ __init__(self, value, next=None, previous=None
        self.value = value
        self.next = next
        self.previous = previous


class LinkedList(object
    ___ __init__(self
        self.head = None
        self._len = 0

    ___ __len__(self
        # faster than le.(list(iter(self))) but requires keeping _len updated
        r_ self._len

    ___ __iter__(self
        p = self.head
        w___ p is not None:
            yield p.previous.value
            p = p.previous
            __ p __ self.head:
                r_

    ___ push(self, value
        self._len += 1
        node = Node(value)
        __ self.head __ None:
            self.head = node.next = node.previous = node
        ____
            node.next, node.previous = self.head, self.head.previous
            self.head.previous.next = self.head.previous = self.head = node

    ___ pop(self
        self._len -= 1
        node = self.head
        __ self.head.next __ self.head:
            self.head = None # Last item
        ____
            node.previous.next = self.head = node.next
            self.head.previous = node.previous
        r_ node.value

    ___ shift(self
        self.head = self.head.previous
        value = self.pop()
        r_ value

    ___ unshift(self, value
        __ self.head is not None:
            self.head = self.head.previous
        self.push(value)
        self.head = self.head.next
