from nose.tools ______ assert_equal


class TestUtopianTree(object

    ___ test_utopian_tree(self
        solution = Solution()
        assert_equal(solution.calc_utopian_tree_height(0), 1)
        assert_equal(solution.calc_utopian_tree_height(1), 2)
        assert_equal(solution.calc_utopian_tree_height(4), 7)
        print('Success: test_utopian_tree')


___ main(
    test = TestUtopianTree()
    test.test_utopian_tree()


__ __name__ __ '__main__':
    main()