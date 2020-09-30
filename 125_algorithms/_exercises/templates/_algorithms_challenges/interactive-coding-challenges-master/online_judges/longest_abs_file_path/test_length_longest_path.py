from nose.tools ______ assert_equal, assert_raises


class TestSolution(object

    ___ test_length_longest_path(self
        solution = Solution()
        assert_raises(TypeError, solution.length_longest_path, None)
        assert_equal(solution.length_longest_path(''), 0)
        file_system = 'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext'
        expected = 32
        assert_equal(solution.length_longest_path(file_system), expected)
        print('Success: test_length_longest_path')


___ main(
    test = TestSolution()
    test.test_length_longest_path()


__  -n __ '__main__':
    main()