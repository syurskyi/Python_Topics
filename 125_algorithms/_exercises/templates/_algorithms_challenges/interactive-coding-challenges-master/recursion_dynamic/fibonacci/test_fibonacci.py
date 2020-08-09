from nose.tools ______ assert_equal


class TestFib(object

    ___ test_fib(self, func
        result = []
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        ___ i in range(le.(expected)):
            result.append(func(i))
        assert_equal(result, expected)
        print('Success: test_fib')


___ main(
    test = TestFib()
    ma__ = Math()
    test.test_fib(ma__.fib_recursive)
    test.test_fib(ma__.fib_dynamic)
    test.test_fib(ma__.fib_iterative)


__ __name__ __ '__main__':
    main()