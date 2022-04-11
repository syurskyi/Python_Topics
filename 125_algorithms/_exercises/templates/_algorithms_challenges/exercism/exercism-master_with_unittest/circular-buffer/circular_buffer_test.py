_______ unittest

____ circular_buffer _______ (
    CircularBuffer,
    BufferFullException,
    BufferEmptyException
)


c_ CircularBufferTest(unittest.TestCase

    ___ test_read_empty_buffer
        buf CircularBuffer(1)
        w__ assertRaises(BufferEmptyException
            buf.r..

    ___ test_write_and_read_back_one_item
        buf CircularBuffer(1)
        buf.w.. '1')
        assertEqual('1', buf.read
        w__ assertRaises(BufferEmptyException
            buf.r..

    ___ test_write_and_read_back_multiple_items
        buf CircularBuffer(2)
        buf.w.. '1')
        buf.w.. '2')
        assertEqual('1', buf.read
        assertEqual('2', buf.read
        w__ assertRaises(BufferEmptyException
            buf.r..

    ___ test_clearing_buffer
        buf CircularBuffer(3)
        ___ c __ '123':
            buf.w.. c)
        buf.clear()
        w__ assertRaises(BufferEmptyException
            buf.r..
        buf.w.. '1')
        buf.w.. '2')
        assertEqual('1', buf.read
        buf.w.. '3')
        assertEqual('2', buf.read

    ___ test_alternate_write_and_read
        buf CircularBuffer(2)
        buf.w.. '1')
        assertEqual('1', buf.read
        buf.w.. '2')
        assertEqual('2', buf.read

    ___ test_read_back_oldest_item
        buf CircularBuffer(3)
        buf.w.. '1')
        buf.w.. '2')
        buf.r..
        buf.w.. '3')
        buf.r..
        assertEqual('3', buf.read

    ___ test_write_full_buffer
        buf CircularBuffer(2)
        buf.w.. '1')
        buf.w.. '2')
        w__ assertRaises(BufferFullException
            buf.w.. 'A')

    ___ test_overwrite_full_buffer
        buf CircularBuffer(2)
        buf.w.. '1')
        buf.w.. '2')
        buf.overwrite('A')
        assertEqual('2', buf.read
        assertEqual('A', buf.read
        w__ assertRaises(BufferEmptyException
            buf.r..

    ___ test_overwrite_non_full_buffer
        buf CircularBuffer(2)
        buf.overwrite('1')
        buf.overwrite('2')
        assertEqual('1', buf.read
        assertEqual('2', buf.read
        w__ assertRaises(BufferEmptyException
            buf.r..

    ___ test_alternate_read_and_overwrite
        buf CircularBuffer(5)
        ___ c __ '123':
            buf.w.. c)
        buf.r..
        buf.r..
        buf.w.. '4')
        buf.r..
        ___ c __ '5678':
            buf.w.. c)
        buf.overwrite('A')
        buf.overwrite('B')
        assertEqual('6', buf.read
        assertEqual('7', buf.read
        assertEqual('8', buf.read
        assertEqual('A', buf.read
        assertEqual('B', buf.read
        w__ assertRaises(BufferEmptyException
            buf.r..


__ _____ __ _____
    unittest.main()
