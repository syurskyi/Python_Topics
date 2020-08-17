______ unittest

from linked_list ______ LinkedList


class LinkedListTests(unittest.TestCase
    ___ setUp(self
        self.list = LinkedList()

    ___ test_push_pop(self
        self.list.push(10)
        self.list.push(20)
        self.assertEqual(self.list.p.., 20)
        self.assertEqual(self.list.p.., 10)

    ___ test_push_shift(self
        self.list.push(10)
        self.list.push(20)
        self.assertEqual(self.list.shift(), 10)
        self.assertEqual(self.list.shift(), 20)

    ___ test_unshift_shift(self
        self.list.unshift(10)
        self.list.unshift(20)
        self.assertEqual(self.list.shift(), 20)
        self.assertEqual(self.list.shift(), 10)

    ___ test_unshift_pop(self
        self.list.unshift(10)
        self.list.unshift(20)
        self.assertEqual(self.list.p.., 10)
        self.assertEqual(self.list.p.., 20)

    ___ test_all(self
        self.list.push(10)
        self.list.push(20)
        self.assertEqual(self.list.p.., 20)
        self.list.push(30)
        self.assertEqual(self.list.shift(), 10)
        self.list.unshift(40)
        self.list.push(50)
        self.assertEqual(self.list.shift(), 40)
        self.assertEqual(self.list.p.., 50)
        self.assertEqual(self.list.shift(), 30)

    @unittest.skip("extra-credit")
    ___ test_length(self
        self.list.push(10)
        self.list.push(20)
        self.assertEqual(le.(self.list), 2)
        self.list.shift()
        self.assertEqual(le.(self.list), 1)
        self.list.p..
        self.assertEqual(le.(self.list), 0)

    @unittest.skip("extra-credit")
    ___ test_iterator(self
        self.list.push(10)
        self.list.push(20)
        iterator = iter(self.list)
        self.assertEqual(next(iterator), 10)
        self.assertEqual(next(iterator), 20)


__ __name__ __ '__main__':
    unittest.main()
