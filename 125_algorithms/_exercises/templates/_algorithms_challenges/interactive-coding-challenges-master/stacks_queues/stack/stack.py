class Node(object

    ___ __init__(self, data, next=None
        self.data = data
        self.next = next


class Stack(object

    ___ __init__(self, top=None
        self.top = top

    ___ push(self, data
        self.top = Node(data, self.top)

    ___ pop(self
        __ self.top is None:
            r_ None
        data = self.top.data
        self.top = self.top.next
        r_ data

    ___ peek(self
        r_ self.top.data __ self.top is not None else None

    ___ is_empty(self
        r_ self.peek() is None