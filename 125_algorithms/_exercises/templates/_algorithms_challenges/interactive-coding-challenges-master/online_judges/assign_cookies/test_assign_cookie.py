from nose.tools ______ assert_equal, assert_raises


class TestAssignCookie(object

    ___ test_assign_cookie(self
        solution = Solution()
        assert_raises(TypeError, solution.find_content_children, None, None)
        assert_equal(solution.find_content_children([1, 2, 3], 
                                                    [1, 1]), 1)
        assert_equal(solution.find_content_children([1, 2], 
                                                    [1, 2, 3]), 2)
        assert_equal(solution.find_content_children([7, 8, 9, 10], 
                                                    [5, 6, 7, 8]), 2)
        print('Success: test_find_content_children')


___ main(
    test = TestAssignCookie()
    test.test_assign_cookie()


__ __name__ __ '__main__':
    main()