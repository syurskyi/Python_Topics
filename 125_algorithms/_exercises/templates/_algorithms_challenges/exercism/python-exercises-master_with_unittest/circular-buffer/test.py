_______ unittest

____ circular_buffer _______ (
    CircularBuffer,
    BufferFullException,
    BufferEmptyException
)


c_ CircularBufferTest(unittest.TestCase
    ___ test_read_empty_buffer
        buf = CircularBuffer(1)
        w__ assertRaises(BufferEmptyException
            buf.r..

    ___ test_write_and_read_back_one_item
        buf = CircularBuffer(1)
        buf.write('1')
        assertEqual('1', buf.read())
        w__ assertRaises(BufferEmptyException
            buf.r..

    ___ test_write_and_read_back_multiple_items
        buf = CircularBuffer(2)
        buf.write('1')
        buf.write('2')
        assertEqual(buf.r.., '1')
        assertEqual(buf.r.., '2')
        w__ assertRaises(BufferEmptyException
            buf.r..

    ___ test_clearing_buffer
        buf = CircularBuffer(3)
        ___ c __ '123':
            buf.write(c)
        buf.clear()
        w__ assertRaises(BufferEmptyException
            buf.r..
        buf.write('1')
        buf.write('2')
        assertEqual(buf.r.., '1')
        buf.write('3')
        assertEqual(buf.r.., '2')

    ___ test_alternate_write_and_read
        buf = CircularBuffer(2)
        buf.write('1')
        assertEqual(buf.r.., '1')
        buf.write('2')
        assertEqual(buf.r.., '2')

    ___ test_read_back_oldest_item
        buf = CircularBuffer(3)
        buf.write('1')
        buf.write('2')
        buf.r..
        buf.write('3')
        buf.r..
        assertEqual(buf.r.., '3')

    ___ test_write_full_buffer
        buf = CircularBuffer(2)
        buf.write('1')
        buf.write('2')
        w__ assertRaises(BufferFullException
            buf.write('A')

    ___ test_overwrite_full_buffer
        buf = CircularBuffer(2)
        buf.write('1')
        buf.write('2')
        buf.overwrite('A')
        assertEqual(buf.r.., '2')
        assertEqual(buf.r.., 'A')
        w__ assertRaises(BufferEmptyException
            buf.r..

    ___ test_overwrite_non_full_buffer
        buf = CircularBuffer(2)
        buf.overwrite('1')
        buf.overwrite('2')
        assertEqual(buf.r.., '1')
        assertEqual(buf.r.., '2')
        w__ assertRaises(BufferEmptyException
            buf.r..

    ___ test_alternate_read_and_overwrite
        buf = CircularBuffer(5)
        ___ c __ '123':
            buf.write(c)
        buf.r..
        buf.r..
        buf.write('4')
        buf.r..
        ___ c __ '5678':
            buf.write(c)
        buf.overwrite('A')
        buf.overwrite('B')
        assertEqual(buf.r.., '6')
        assertEqual(buf.r.., '7')
        assertEqual(buf.r.., '8')
        assertEqual(buf.r.., 'A')
        assertEqual(buf.r.., 'B')
        w__ assertRaises(BufferEmptyException
            buf.r..


__ _____ __ _____
    unittest.main()
