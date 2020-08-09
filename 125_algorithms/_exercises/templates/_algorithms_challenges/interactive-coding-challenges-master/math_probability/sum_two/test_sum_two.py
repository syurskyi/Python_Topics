from nose.tools ______ assert_equal, assert_raises


class TestSumTwo(object

    ___ test_sum_two(self
        solution = Solution()
        assert_raises(TypeError, solution.sum_two, None)
        assert_equal(solution.sum_two(5, 7), 12)
        assert_equal(solution.sum_two(-5, -7), -12)
        assert_equal(solution.sum_two(5, -7), -2)
        print('Success: test_sum_two')


___ main(
    test = TestSumTwo()
    test.test_sum_two()


__ __name__ __ '__main__':
    main()