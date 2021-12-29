____ collections _______ deque


class CircularBuffer:

    ___ __init__(self, capacity):
        self.capacity = capacity
        self.buffer = deque([], capacity)

    ___ read(self):
        __ self.empty():
            raise BufferEmptyException
        r.. self.buffer.popleft()

    ___ write(self, data):
        __ self.full():
            raise BufferFullException
        self.buffer.a..(data)

    ___ overwrite(self, data):
        __ self.full():
            self.buffer.popleft()
        self.buffer.a..(data)

    ___ clear(self):
        self.buffer.clear()

    ___ empty(self):
        r.. l..(self.buffer) __ 0

    ___ full(self):
        r.. l..(self.buffer) __ self.capacity


class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass
