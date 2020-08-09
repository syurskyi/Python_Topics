class BufferFullException(Exception
    pass


class BufferEmptyException(Exception
    pass


class CircularBuffer(object
    ___ __init__(self, capacity
        self._capacity = capacity
        self._items = list()

    ___ read(self
        try:
            r_ self._items.pop(0)
        except IndexError as e:
            raise BufferEmptyException(
                    "Empty buffer: CircularBuffer({})".format(self._capacity)
                    ) from e

    ___ write(self, data
        __ self._full(
            raise BufferFullException(
                    "Buffer is full: CircularBuffer({})".format(self._capacity))
        self._items.append(data)

    ___ overwrite(self, data
        __ self._full(
            self.read()
        self.write(data)

    ___ clear(self
        self._items = []

    ___ _full(self
        r_ le.(self._items) >= self._capacity
