____ collections _______ deque


c_ CircularBuffer:

    ___ - , capacity):
        capacity = capacity
        buffer = deque([], capacity)

    ___ read
        __ empty
            r.. BufferEmptyException
        r.. buffer.popleft()

    ___ write(self, data):
        __ full
            r.. BufferFullException
        buffer.a..(data)

    ___ overwrite(self, data):
        __ full
            buffer.popleft()
        buffer.a..(data)

    ___ clear
        buffer.clear()

    ___ empty
        r.. l..(buffer) __ 0

    ___ full
        r.. l..(buffer) __ capacity


c_ BufferFullException(Exception):
    p..


c_ BufferEmptyException(Exception):
    p..
