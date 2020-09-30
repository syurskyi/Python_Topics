from nose.tools ______ assert_equal, assert_raises


class TestFizzBuzz(object

    ___ test_fizz_buzz(self
        solution = Solution()
        assert_raises(TypeError, solution.fizz_buzz, None)
        assert_raises(ValueError, solution.fizz_buzz, 0)
        expected = [
            '1',
            '2',
            'Fizz',
            '4',
            'Buzz',
            'Fizz',
            '7',
            '8',
            'Fizz',
            'Buzz',
            '11',
            'Fizz',
            '13',
            '14',
            'FizzBuzz'
        ]
        assert_equal(solution.fizz_buzz(15), expected)
        print('Success: test_fizz_buzz')


___ main(
    test = TestFizzBuzz()
    test.test_fizz_buzz()


__  -n __ '__main__':
    main()