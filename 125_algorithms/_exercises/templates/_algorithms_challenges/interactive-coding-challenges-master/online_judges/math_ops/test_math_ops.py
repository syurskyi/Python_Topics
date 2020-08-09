from nose.tools ______ assert_equal, assert_true, assert_raises


class TestMathOps(object

    ___ test_math_ops(self
        solution = Solution()
        assert_raises(TypeError, solution.insert, None)
        solution.insert(5)
        solution.insert(2)
        solution.insert(7)
        solution.insert(9)
        solution.insert(9)
        solution.insert(2)
        solution.insert(9)
        solution.insert(4)
        solution.insert(3)
        solution.insert(3)
        solution.insert(2)
        assert_equal(solution.max, 9)
        assert_equal(solution.min, 2)
        assert_equal(solution.mean, 5)
        assert_true(solution.mode in (2, 92))
        print('Success: test_math_ops')


___ main(
    test = TestMathOps()
    test.test_math_ops()


__ __name__ __ '__main__':
    main()