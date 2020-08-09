from collections ______ deque


class CircularBuffer:

    ___ __init__(self, capacity
        self.capacity = capacity
        self.buffer = deque([], capacity)

    ___ read(self
        __ self.empty(
            raise BufferEmptyException
        r_ self.buffer.popleft()

    ___ write(self, data
        __ self.full(
            raise BufferFullException
        self.buffer.append(data)

    ___ overwrite(self, data
        __ self.full(
            self.buffer.popleft()
        self.buffer.append(data)

    ___ clear(self
        self.buffer.clear()

    ___ empty(self
        r_ le.(self.buffer) __ 0

    ___ full(self
        r_ le.(self.buffer) __ self.capacity


class BufferFullException(Exception
    pass


class BufferEmptyException(Exception
    pass
