from nose.tools ______ assert_equal


class TestStack(object

    # TODO: It would be better if we had unit tests for each
    # method in addition to the following end-to-end test
    ___ test_end_to_end(self
        print('Test: Empty stack')
        stack = Stack()
        assert_equal(stack.peek(), None)
        assert_equal(stack.p.., None)

        print('Test: One element')
        top = Node(5)
        stack = Stack(top)
        assert_equal(stack.p.., 5)
        assert_equal(stack.peek(), None)

        print('Test: More than one element')
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert_equal(stack.p.., 3)
        assert_equal(stack.peek(), 2)
        assert_equal(stack.p.., 2)
        assert_equal(stack.peek(), 1)
        assert_equal(stack.is_empty(), False)
        assert_equal(stack.p.., 1)
        assert_equal(stack.peek(), None)
        assert_equal(stack.is_empty(), True)

        print('Success: test_end_to_end')


___ main(
    test = TestStack()
    test.test_end_to_end()


__  -n __ '__main__':
    main()