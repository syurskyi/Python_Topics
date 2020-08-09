from nose.tools ______ assert_equal, assert_raises


class TestMergeRanges(object

    ___ test_merge_ranges(self
        solution = Solution()
        assert_raises(TypeError, solution.merge_ranges, None)
        assert_equal(solution.merge_ranges([]), [])
        array = [(2, 3), (7, 9)]
        expected = [(2, 3), (7, 9)]
        assert_equal(solution.merge_ranges(array), expected)
        array = [(3, 5), (2, 3), (7, 9), (8, 10)]
        expected = [(2, 5), (7, 10)]
        assert_equal(solution.merge_ranges(array), expected)
        array = [(2, 3), (3, 5), (7, 9), (8, 10), (1, 11)]
        expected = [(1, 11)]
        assert_equal(solution.merge_ranges(array), expected)
        print('Success: test_merge_ranges')


___ main(
    test = TestMergeRanges()
    test.test_merge_ranges()


__ __name__ __ '__main__':
    main()