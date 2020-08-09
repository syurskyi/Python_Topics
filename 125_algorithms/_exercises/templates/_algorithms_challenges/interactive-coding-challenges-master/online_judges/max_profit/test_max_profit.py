from nose.tools ______ assert_equal, assert_raises


class TestMaxProfit(object

    ___ test_max_profit(self
        solution = Solution()
        assert_raises(TypeError, solution.find_max_profit, None)
        assert_raises(ValueError, solution.find_max_profit, [])
        assert_equal(solution.find_max_profit([8, 5, 3, 2, 1]), -1)
        assert_equal(solution.find_max_profit([5, 3, 7, 4, 2, 6, 9]), 7)
        print('Success: test_max_profit')


___ main(
    test = TestMaxProfit()
    test.test_max_profit()


__ __name__ __ '__main__':
    main()