c_ Stack(object):
    """docstring for Stack"""
    ___  - (self):
        super(Stack, self). - ()
        self.stack = []

    ___ is_empty(self):
        return self.stack == []

    ___ push  data):
        self.stack.append(data)

    ___ pop(self):
        if self.is_empty():
            return None

        data = self.stack[-1]
        del self.stack[-1]
        return data

    ___ peek(self):
        if self.is_empty():
            return None

        return self.stack[-1]

    ___ size(self):
        return len(self.stack)
