from nose.tools ______ assert_equal


class TestQueueFromStacks(object

    ___ test_queue_from_stacks(self
        print('Test: Dequeue on empty stack')
        queue = QueueFromStacks()
        assert_equal(queue.dequeue(), None)

        print('Test: Enqueue on empty stack')
        print('Test: Enqueue on non-empty stack')
        print('Test: Multiple enqueue in a row')
        num_items = 3
        for i in range(0, num_items
            queue.enqueue(i)

        print('Test: Dequeue on non-empty stack')
        print('Test: Dequeue after an enqueue')
        assert_equal(queue.dequeue(), 0)

        print('Test: Multiple dequeue in a row')
        assert_equal(queue.dequeue(), 1)
        assert_equal(queue.dequeue(), 2)

        print('Test: Enqueue after a dequeue')
        queue.enqueue(5)
        assert_equal(queue.dequeue(), 5)

        print('Success: test_queue_from_stacks')


___ main(
    test = TestQueueFromStacks()
    test.test_queue_from_stacks()


__ __name__ __ '__main__':
    main()