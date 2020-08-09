from nose.tools ______ assert_equal, assert_raises


class TestFindDiff(object

    ___ test_find_diff(self
        solution = Solution()
        assert_raises(TypeError, solution.find_diff, None)
        assert_equal(solution.find_diff('aaabbcdd', 'abdbacade'), 'e')
        print('Success: test_find_diff')


___ main(
    test = TestFindDiff()
    test.test_find_diff()


__ __name__ __ '__main__':
    main()