______ unittest

from linked_list ______ LinkedList


class LinkedListTest(unittest.TestCase
    ___ test_push_pop(self
        lst = LinkedList()
        lst.push(10)
        lst.push(20)
        self.assertEqual(lst.p.., 20)
        self.assertEqual(lst.p.., 10)

    ___ test_push_shift(self
        lst = LinkedList()
        lst.push(10)
        lst.push(20)
        self.assertEqual(lst.shift(), 10)
        self.assertEqual(lst.shift(), 20)

    ___ test_unshift_shift(self
        lst = LinkedList()
        lst.unshift(10)
        lst.unshift(20)
        self.assertEqual(lst.shift(), 20)
        self.assertEqual(lst.shift(), 10)

    ___ test_unshift_pop(self
        lst = LinkedList()
        lst.unshift(10)
        lst.unshift(20)
        self.assertEqual(lst.p.., 10)
        self.assertEqual(lst.p.., 20)

    ___ test_all(self
        lst = LinkedList()
        lst.push(10)
        lst.push(20)
        self.assertEqual(lst.p.., 20)
        lst.push(30)
        self.assertEqual(lst.shift(), 10)
        lst.unshift(40)
        lst.push(50)
        self.assertEqual(lst.shift(), 40)
        self.assertEqual(lst.p.., 50)
        self.assertEqual(lst.shift(), 30)

    ___ test_length(self
        lst = LinkedList()
        lst.push(10)
        lst.push(20)
        self.assertEqual(le.(lst), 2)
        lst.shift()
        self.assertEqual(le.(lst), 1)
        lst.p..
        self.assertEqual(le.(lst), 0)

    @unittest.skip("extra-credit")
    ___ test_iterator(self
        lst = LinkedList()
        lst.push(10)
        lst.push(20)
        iterator = iter(lst)
        self.assertEqual(next(iterator), 10)
        self.assertEqual(next(iterator), 20)


__  -n __ '__main__':
    unittest.main()
