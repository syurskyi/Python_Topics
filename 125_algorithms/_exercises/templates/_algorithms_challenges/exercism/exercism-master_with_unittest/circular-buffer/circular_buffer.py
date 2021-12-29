from collections import deque


class CircularBuffer:

    ___ __init__(self, capacity):
        self.capacity = capacity
        self.buffer = deque([], capacity)

    ___ read(self):
        __ self.empty():
            raise BufferEmptyException
        return self.buffer.popleft()

    ___ write(self, data):
        __ self.full():
            raise BufferFullException
        self.buffer.append(data)

    ___ overwrite(self, data):
        __ self.full():
            self.buffer.popleft()
        self.buffer.append(data)

    ___ clear(self):
        self.buffer.clear()

    ___ empty(self):
        return len(self.buffer) == 0

    ___ full(self):
        return len(self.buffer) == self.capacity


class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass
