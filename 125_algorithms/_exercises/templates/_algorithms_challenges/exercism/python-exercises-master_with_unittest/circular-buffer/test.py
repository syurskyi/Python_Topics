_______ unittest

____ circular_buffer _______ (
    CircularBuffer,
    BufferFullException,
    BufferEmptyException
)


c_ CircularBufferTest(unittest.TestCase):
    ___ test_read_empty_buffer
        buf = CircularBuffer(1)
        w__ assertRaises(BufferEmptyException):
            buf.read()

    ___ test_write_and_read_back_one_item
        buf = CircularBuffer(1)
        buf.write('1')
        assertEqual('1', buf.read())
        w__ assertRaises(BufferEmptyException):
            buf.read()

    ___ test_write_and_read_back_multiple_items
        buf = CircularBuffer(2)
        buf.write('1')
        buf.write('2')
        assertEqual(buf.read(), '1')
        assertEqual(buf.read(), '2')
        w__ assertRaises(BufferEmptyException):
            buf.read()

    ___ test_clearing_buffer
        buf = CircularBuffer(3)
        ___ c __ '123':
            buf.write(c)
        buf.clear()
        w__ assertRaises(BufferEmptyException):
            buf.read()
        buf.write('1')
        buf.write('2')
        assertEqual(buf.read(), '1')
        buf.write('3')
        assertEqual(buf.read(), '2')

    ___ test_alternate_write_and_read
        buf = CircularBuffer(2)
        buf.write('1')
        assertEqual(buf.read(), '1')
        buf.write('2')
        assertEqual(buf.read(), '2')

    ___ test_read_back_oldest_item
        buf = CircularBuffer(3)
        buf.write('1')
        buf.write('2')
        buf.read()
        buf.write('3')
        buf.read()
        assertEqual(buf.read(), '3')

    ___ test_write_full_buffer
        buf = CircularBuffer(2)
        buf.write('1')
        buf.write('2')
        w__ assertRaises(BufferFullException):
            buf.write('A')

    ___ test_overwrite_full_buffer
        buf = CircularBuffer(2)
        buf.write('1')
        buf.write('2')
        buf.overwrite('A')
        assertEqual(buf.read(), '2')
        assertEqual(buf.read(), 'A')
        w__ assertRaises(BufferEmptyException):
            buf.read()

    ___ test_overwrite_non_full_buffer
        buf = CircularBuffer(2)
        buf.overwrite('1')
        buf.overwrite('2')
        assertEqual(buf.read(), '1')
        assertEqual(buf.read(), '2')
        w__ assertRaises(BufferEmptyException):
            buf.read()

    ___ test_alternate_read_and_overwrite
        buf = CircularBuffer(5)
        ___ c __ '123':
            buf.write(c)
        buf.read()
        buf.read()
        buf.write('4')
        buf.read()
        ___ c __ '5678':
            buf.write(c)
        buf.overwrite('A')
        buf.overwrite('B')
        assertEqual(buf.read(), '6')
        assertEqual(buf.read(), '7')
        assertEqual(buf.read(), '8')
        assertEqual(buf.read(), 'A')
        assertEqual(buf.read(), 'B')
        w__ assertRaises(BufferEmptyException):
            buf.read()


__ _____ __ _____
    unittest.main()
