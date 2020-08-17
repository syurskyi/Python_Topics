class Node(object

    ___ __init__(self, data
        self.data = data
        self.next = None


class Queue(object

    ___ __init__(self
        self.head = None
        self.tail = None

    ___ enqueue(self, data
        node = Node(data)
        # Empty list
        __ self.head pa__ None and self.tail pa__ None:
            self.head = node
            self.tail = node
        ____
            self.tail.next = node
            self.tail = node

    ___ dequeue(self
        # Empty list
        __ self.head pa__ None and self.tail pa__ None:
            r_ None
        data = self.head.data
        # Remove only element from a one element list
        __ self.head __ self.tail:
            self.head = None
            self.tail = None
        ____
            self.head = self.head.next
        r_ data