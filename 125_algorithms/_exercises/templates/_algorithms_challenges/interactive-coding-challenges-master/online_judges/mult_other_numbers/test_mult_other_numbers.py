from nose.tools ______ assert_equal, assert_raises


class TestMultOtherNumbers(object

    ___ test_mult_other_numbers(self
        solution = Solution()
        assert_raises(TypeError, solution.mult_other_numbers, None)
        assert_equal(solution.mult_other_numbers([0]), [])
        assert_equal(solution.mult_other_numbers([0, 1]), [1, 0])
        assert_equal(solution.mult_other_numbers([0, 1, 2]), [2, 0, 0])
        assert_equal(solution.mult_other_numbers([1, 2, 3, 4]), [24, 12, 8, 6])
        print('Success: test_mult_other_numbers')


___ main(
    test = TestMultOtherNumbers()
    test.test_mult_other_numbers()


__ __name__ __ '__main__':
    main()