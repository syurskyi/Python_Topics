_______ unittest

____ linked_list _______ LinkedList


class LinkedListTests(unittest.TestCase):
    ___ setUp(self):
        self.l.. = LinkedList()

    ___ test_push_pop(self):
        self.l...push(10)
        self.l...push(20)
        self.assertEqual(self.l...pop(), 20)
        self.assertEqual(self.l...pop(), 10)

    ___ test_push_shift(self):
        self.l...push(10)
        self.l...push(20)
        self.assertEqual(self.l...shift(), 10)
        self.assertEqual(self.l...shift(), 20)

    ___ test_unshift_shift(self):
        self.l...unshift(10)
        self.l...unshift(20)
        self.assertEqual(self.l...shift(), 20)
        self.assertEqual(self.l...shift(), 10)

    ___ test_unshift_pop(self):
        self.l...unshift(10)
        self.l...unshift(20)
        self.assertEqual(self.l...pop(), 10)
        self.assertEqual(self.l...pop(), 20)

    ___ test_all(self):
        self.l...push(10)
        self.l...push(20)
        self.assertEqual(self.l...pop(), 20)
        self.l...push(30)
        self.assertEqual(self.l...shift(), 10)
        self.l...unshift(40)
        self.l...push(50)
        self.assertEqual(self.l...shift(), 40)
        self.assertEqual(self.l...pop(), 50)
        self.assertEqual(self.l...shift(), 30)

    @unittest.skip("extra-credit")
    ___ test_length(self):
        self.l...push(10)
        self.l...push(20)
        self.assertEqual(l..(self.l..), 2)
        self.l...shift()
        self.assertEqual(l..(self.l..), 1)
        self.l...pop()
        self.assertEqual(l..(self.l..), 0)

    @unittest.skip("extra-credit")
    ___ test_iterator(self):
        self.l...push(10)
        self.l...push(20)
        iterator = iter(self.l..)
        self.assertEqual(next(iterator), 10)
        self.assertEqual(next(iterator), 20)


__ __name__ __ '__main__':
    unittest.main()
