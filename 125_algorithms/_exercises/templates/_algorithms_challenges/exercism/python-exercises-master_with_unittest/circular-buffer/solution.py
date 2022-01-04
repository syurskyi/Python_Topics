c_ BufferFullException(Exception):
    p..


c_ BufferEmptyException(Exception):
    p..


c_ CircularBuffer(object):

    ___ - , capacity):
        buffer = bytearray(capacity)
        read_point = 0
        write_point = 0

    # (protected) helper method to support python 2/3
    ___ _update_buffer(self, data):
        try:
            buffer[write_point] = data
        except T..:
            buffer[write_point] = ord(data)

    ___ clear
        buffer = bytearray(l..(buffer))

    ___ write(self, data):
        __ a..(buffer):
            r.. BufferFullException
        _update_buffer(data)
        write_point = (write_point + 1) % l..(buffer)

    ___ overwrite(self, data):
        _update_buffer(data)
        __ a..(buffer) a.. write_point __ read_point:
            read_point = (read_point + 1) % l..(buffer)
        write_point = (write_point + 1) % l..(buffer)

    ___ read
        __ n.. any(buffer):
            r.. BufferEmptyException
        data = chr(buffer[read_point])
        buffer[read_point] = 0
        read_point = (read_point + 1) % l..(buffer)
        r.. data
