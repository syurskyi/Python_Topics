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
        self.buffer = bytearray(l..(self.buffer))

    ___ write(self, data):
        __ a..(self.buffer):
            raise BufferFullException
        self._update_buffer(data)
        self.write_point = (self.write_point + 1) % l..(self.buffer)

    ___ overwrite(self, data):
        self._update_buffer(data)
        __ a..(self.buffer) a.. self.write_point __ self.read_point:
            self.read_point = (self.read_point + 1) % l..(self.buffer)
        self.write_point = (self.write_point + 1) % l..(self.buffer)

    ___ read(self):
        __ n.. any(self.buffer):
            raise BufferEmptyException
        data = chr(self.buffer[self.read_point])
        self.buffer[self.read_point] = 0
        self.read_point = (self.read_point + 1) % l..(self.buffer)
        r.. data
