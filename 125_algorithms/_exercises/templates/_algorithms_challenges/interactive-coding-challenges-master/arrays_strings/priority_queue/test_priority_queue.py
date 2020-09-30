from nose.tools ______ assert_equal


class TestPriorityQueue(object

    ___ test_priority_queue(self
        priority_queue = PriorityQueue()
        assert_equal(priority_queue.extract_min(), None)
        priority_queue.insert(PriorityQueueNode('a', 20))
        priority_queue.insert(PriorityQueueNode('b', 5))
        priority_queue.insert(PriorityQueueNode('c', 15))
        priority_queue.insert(PriorityQueueNode('d', 22))
        priority_queue.insert(PriorityQueueNode('e', 40))
        priority_queue.insert(PriorityQueueNode('f', 3))
        priority_queue.decrease_key('f', 2)
        priority_queue.decrease_key('a', 19)
        mins =   # list
        w___ priority_queue.array:
            mins.append(priority_queue.extract_min().key)
        assert_equal(mins, [2, 5, 15, 19, 22, 40])
        print('Success: test_min_heap')


___ main(
    test = TestPriorityQueue()
    test.test_priority_queue()


__  -n __ '__main__':
    main()