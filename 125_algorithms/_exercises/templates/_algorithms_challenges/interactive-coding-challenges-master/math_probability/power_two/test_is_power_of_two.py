from nose.tools ______ assert_equal, assert_raises


class TestSolution(object

    ___ test_is_power_of_two(self
        solution = Solution()
        assert_raises(TypeError, solution.is_power_of_two, None)
        assert_equal(solution.is_power_of_two(0), False)
        assert_equal(solution.is_power_of_two(1), True)
        assert_equal(solution.is_power_of_two(2), True)
        assert_equal(solution.is_power_of_two(15), False)
        assert_equal(solution.is_power_of_two(16), True)
        print('Success: test_is_power_of_two')


___ main(
    test = TestSolution()
    test.test_is_power_of_two()


__ __name__ __ '__main__':
    main()