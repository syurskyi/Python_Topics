____ c.. _______ d..


c_ CircularBuffer:

    ___ - , capacity
        capacity = capacity
        buffer = d..([], capacity)

    ___ read
        __ empty
            r.. BufferEmptyException
        r.. buffer.popleft()

    ___ write  data
        __ full
            r.. BufferFullException
        buffer.a..(data)

    ___ overwrite  data
        __ full
            buffer.popleft()
        buffer.a..(data)

    ___ clear
        buffer.clear()

    ___ empty
        r.. l..(buffer) __ 0

    ___ full
        r.. l..(buffer) __ capacity


c_ BufferFullException(E..
    p..


c_ BufferEmptyException(E..
    p..
