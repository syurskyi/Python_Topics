_______ unittest

____ linked_list _______ LinkedList


c_ LinkedListTest(unittest.TestCase):
    ___ test_push_pop
        lst = LinkedList()
        lst.push(10)
        lst.push(20)
        assertEqual(lst.pop(), 20)
        assertEqual(lst.pop(), 10)

    ___ test_push_shift
        lst = LinkedList()
        lst.push(10)
        lst.push(20)
        assertEqual(lst.shift(), 10)
        assertEqual(lst.shift(), 20)

    ___ test_unshift_shift
        lst = LinkedList()
        lst.unshift(10)
        lst.unshift(20)
        assertEqual(lst.shift(), 20)
        assertEqual(lst.shift(), 10)

    ___ test_unshift_pop
        lst = LinkedList()
        lst.unshift(10)
        lst.unshift(20)
        assertEqual(lst.pop(), 10)
        assertEqual(lst.pop(), 20)

    ___ test_all
        lst = LinkedList()
        lst.push(10)
        lst.push(20)
        assertEqual(lst.pop(), 20)
        lst.push(30)
        assertEqual(lst.shift(), 10)
        lst.unshift(40)
        lst.push(50)
        assertEqual(lst.shift(), 40)
        assertEqual(lst.pop(), 50)
        assertEqual(lst.shift(), 30)

    ___ test_length
        lst = LinkedList()
        lst.push(10)
        lst.push(20)
        assertEqual(l..(lst), 2)
        lst.shift()
        assertEqual(l..(lst), 1)
        lst.pop()
        assertEqual(l..(lst), 0)

    @unittest.skip("extra-credit")
    ___ test_iterator
        lst = LinkedList()
        lst.push(10)
        lst.push(20)
        iterator = i..(lst)
        assertEqual(next(iterator), 10)
        assertEqual(next(iterator), 20)


__ __name__ __ '__main__':
    unittest.main()
