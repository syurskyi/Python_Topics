______ unittest

from circular_buffer ______ (
    CircularBuffer,
    BufferFullException,
    BufferEmptyException
)


class CircularBufferTest(unittest.TestCase
    ___ test_read_empty_buffer(self
        buf = CircularBuffer(1)
        with self.assertRaises(BufferEmptyException
            buf.read()

    ___ test_write_and_read_back_one_item(self
        buf = CircularBuffer(1)
        buf.write('1')
        self.assertEqual('1', buf.read())
        with self.assertRaises(BufferEmptyException
            buf.read()

    ___ test_write_and_read_back_multiple_items(self
        buf = CircularBuffer(2)
        buf.write('1')
        buf.write('2')
        self.assertEqual(buf.read(), '1')
        self.assertEqual(buf.read(), '2')
        with self.assertRaises(BufferEmptyException
            buf.read()

    ___ test_clearing_buffer(self
        buf = CircularBuffer(3)
        ___ c __ '123':
            buf.write(c)
        buf.clear()
        with self.assertRaises(BufferEmptyException
            buf.read()
        buf.write('1')
        buf.write('2')
        self.assertEqual(buf.read(), '1')
        buf.write('3')
        self.assertEqual(buf.read(), '2')

    ___ test_alternate_write_and_read(self
        buf = CircularBuffer(2)
        buf.write('1')
        self.assertEqual(buf.read(), '1')
        buf.write('2')
        self.assertEqual(buf.read(), '2')

    ___ test_read_back_oldest_item(self
        buf = CircularBuffer(3)
        buf.write('1')
        buf.write('2')
        buf.read()
        buf.write('3')
        buf.read()
        self.assertEqual(buf.read(), '3')

    ___ test_write_full_buffer(self
        buf = CircularBuffer(2)
        buf.write('1')
        buf.write('2')
        with self.assertRaises(BufferFullException
            buf.write('A')

    ___ test_overwrite_full_buffer(self
        buf = CircularBuffer(2)
        buf.write('1')
        buf.write('2')
        buf.overwrite('A')
        self.assertEqual(buf.read(), '2')
        self.assertEqual(buf.read(), 'A')
        with self.assertRaises(BufferEmptyException
            buf.read()

    ___ test_overwrite_non_full_buffer(self
        buf = CircularBuffer(2)
        buf.overwrite('1')
        buf.overwrite('2')
        self.assertEqual(buf.read(), '1')
        self.assertEqual(buf.read(), '2')
        with self.assertRaises(BufferEmptyException
            buf.read()

    ___ test_alternate_read_and_overwrite(self
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
        self.assertEqual(buf.read(), '6')
        self.assertEqual(buf.read(), '7')
        self.assertEqual(buf.read(), '8')
        self.assertEqual(buf.read(), 'A')
        self.assertEqual(buf.read(), 'B')
        with self.assertRaises(BufferEmptyException
            buf.read()


__  -n __ '__main__':
    unittest.main()
