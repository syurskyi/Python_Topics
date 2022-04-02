c_ BufferFullException(E..
    p..


c_ BufferEmptyException(E..
    p..


c_ CircularBuffer(o..

    ___ - , capacity
        buffer = bytearray(capacity)
        read_point = 0
        write_point = 0

    # (protected) helper method to support python 2/3
    ___ _update_buffer  data
        ___
            buffer[write_point] = data
        ______ T..:
            buffer[write_point] = o..(data)

    ___ clear
        buffer = bytearray(l..(buffer))

    ___ write  data
        __ a..(buffer
            r.. BufferFullException
        _update_buffer(data)
        write_point = (write_point + 1) % l..(buffer)

    ___ overwrite  data
        _update_buffer(data)
        __ a..(buffer) a.. write_point __ read_point:
            read_point = (read_point + 1) % l..(buffer)
        write_point = (write_point + 1) % l..(buffer)

    ___ read
        __ n.. any(buffer
            r.. BufferEmptyException
        data = chr(buffer[read_point])
        buffer[read_point] = 0
        read_point = (read_point + 1) % l..(buffer)
        r.. data
