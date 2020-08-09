from nose.tools ______ assert_equal, assert_raises


class TestProdThree(object

    ___ test_prod_three(self
        solution = Solution()
        assert_raises(TypeError, solution.max_prod_three, None)
        assert_raises(ValueError, solution.max_prod_three, [1, 2])
        assert_equal(solution.max_prod_three([5, -2, 3]), -30)
        assert_equal(solution.max_prod_three([5, -2, 3, 1, -1, 4]), 60)
        print('Success: test_prod_three')


___ main(
    test = TestProdThree()
    test.test_prod_three()


__ __name__ __ '__main__':
    main()