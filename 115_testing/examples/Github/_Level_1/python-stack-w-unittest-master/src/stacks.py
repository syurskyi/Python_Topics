class Stack(object):
    """docstring for Stack"""
    def __init__(self):
        super(Stack, self).__init__()
        self.stack = []

    def is_empty(self):
        return self.stack == []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            return None

        data = self.stack[-1]
        del self.stack[-1]
        return data

    def peek(self):
        if self.is_empty():
            return None

        return self.stack[-1]

    def size(self):
        return len(self.stack)
