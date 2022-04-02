_______ unittest

____ linked_list _______ LinkedList


c_ LinkedListTests(unittest.TestCase
    ___ setUp
        l.. = LinkedList()

    ___ test_push_pop
        l...push(10)
        l...push(20)
        assertEqual(l...pop(), 20)
        assertEqual(l...pop(), 10)

    ___ test_push_shift
        l...push(10)
        l...push(20)
        assertEqual(l...shift(), 10)
        assertEqual(l...shift(), 20)

    ___ test_unshift_shift
        l...unshift(10)
        l...unshift(20)
        assertEqual(l...shift(), 20)
        assertEqual(l...shift(), 10)

    ___ test_unshift_pop
        l...unshift(10)
        l...unshift(20)
        assertEqual(l...pop(), 10)
        assertEqual(l...pop(), 20)

    ___ test_all
        l...push(10)
        l...push(20)
        assertEqual(l...pop(), 20)
        l...push(30)
        assertEqual(l...shift(), 10)
        l...unshift(40)
        l...push(50)
        assertEqual(l...shift(), 40)
        assertEqual(l...pop(), 50)
        assertEqual(l...shift(), 30)

    @unittest.skip("extra-credit")
    ___ test_length
        l...push(10)
        l...push(20)
        assertEqual(l..(l..), 2)
        l...shift()
        assertEqual(l..(l..), 1)
        l...pop()
        assertEqual(l..(l..), 0)

    @unittest.skip("extra-credit")
    ___ test_iterator
        l...push(10)
        l...push(20)
        iterator = i..(l..)
        assertEqual(next(iterator), 10)
        assertEqual(next(iterator), 20)


__ _____ __ _____
    unittest.main()
