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
        self.assertEqual('1', buf.read())
        self.assertEqual('2', buf.read())
        with self.assertRaises(BufferEmptyException
            buf.read()

    ___ test_clearing_buffer(self
        buf = CircularBuffer(3)
        ___ c in '123':
            buf.write(c)
        buf.clear()
        with self.assertRaises(BufferEmptyException
            buf.read()
        buf.write('1')
        buf.write('2')
        self.assertEqual('1', buf.read())
        buf.write('3')
        self.assertEqual('2', buf.read())

    ___ test_alternate_write_and_read(self
        buf = CircularBuffer(2)
        buf.write('1')
        self.assertEqual('1', buf.read())
        buf.write('2')
        self.assertEqual('2', buf.read())

    ___ test_read_back_oldest_item(self
        buf = CircularBuffer(3)
        buf.write('1')
        buf.write('2')
        buf.read()
        buf.write('3')
        buf.read()
        self.assertEqual('3', buf.read())

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
        self.assertEqual('2', buf.read())
        self.assertEqual('A', buf.read())
        with self.assertRaises(BufferEmptyException
            buf.read()

    ___ test_overwrite_non_full_buffer(self
        buf = CircularBuffer(2)
        buf.overwrite('1')
        buf.overwrite('2')
        self.assertEqual('1', buf.read())
        self.assertEqual('2', buf.read())
        with self.assertRaises(BufferEmptyException
            buf.read()

    ___ test_alternate_read_and_overwrite(self
        buf = CircularBuffer(5)
        ___ c in '123':
            buf.write(c)
        buf.read()
        buf.read()
        buf.write('4')
        buf.read()
        ___ c in '5678':
            buf.write(c)
        buf.overwrite('A')
        buf.overwrite('B')
        self.assertEqual('6', buf.read())
        self.assertEqual('7', buf.read())
        self.assertEqual('8', buf.read())
        self.assertEqual('A', buf.read())
        self.assertEqual('B', buf.read())
        with self.assertRaises(BufferEmptyException
            buf.read()


__ __name__ __ '__main__':
    unittest.main()
