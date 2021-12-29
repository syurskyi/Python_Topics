class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer(object):

    ___ __init__(self, capacity):
        self.buffer = bytearray(capacity)
        self.read_point = 0
        self.write_point = 0

    # (protected) helper method to support python 2/3
    ___ _update_buffer(self, data):
        try:
            self.buffer[self.write_point] = data
        except TypeError:
            self.buffer[self.write_point] = ord(data)

    ___ clear(self):
        self.buffer = bytearray(len(self.buffer))

    ___ write(self, data):
        __ all(self.buffer):
            raise BufferFullException
        self._update_buffer(data)
        self.write_point = (self.write_point + 1) % len(self.buffer)

    ___ overwrite(self, data):
        self._update_buffer(data)
        __ all(self.buffer) and self.write_point == self.read_point:
            self.read_point = (self.read_point + 1) % len(self.buffer)
        self.write_point = (self.write_point + 1) % len(self.buffer)

    ___ read(self):
        __ not any(self.buffer):
            raise BufferEmptyException
        data = chr(self.buffer[self.read_point])
        self.buffer[self.read_point] = 0
        self.read_point = (self.read_point + 1) % len(self.buffer)
        return data
