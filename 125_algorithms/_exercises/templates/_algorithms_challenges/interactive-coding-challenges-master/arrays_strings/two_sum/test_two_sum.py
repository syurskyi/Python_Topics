from nose.tools ______ assert_equal, assert_raises


class TestTwoSum(object

    ___ test_two_sum(self
        solution = Solution()
        assert_raises(TypeError, solution.two_sum, None, None)
        assert_raises(ValueError, solution.two_sum,   # list, 0)
        target = 7
        nums = [1, 3, 2, -7, 5]
        expected = [2, 4]
        assert_equal(solution.two_sum(nums, target), expected)
        print('Success: test_two_sum')


___ main(
    test = TestTwoSum()
    test.test_two_sum()


__  -n __ '__main__':
    main()