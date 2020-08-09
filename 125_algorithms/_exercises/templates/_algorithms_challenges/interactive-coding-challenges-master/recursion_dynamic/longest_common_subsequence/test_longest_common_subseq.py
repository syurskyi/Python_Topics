from nose.tools ______ assert_equal, assert_raises


class TestLongestCommonSubseq(object

    ___ test_longest_common_subseq(self
        str_comp = StringCompare()
        assert_raises(TypeError, str_comp.longest_common_subseq, None, None)
        assert_equal(str_comp.longest_common_subseq('', ''), '')
        str0 = 'ABCDEFGHIJ'
        str1 = 'FOOBCDBCDE'
        expected = 'BCDE'
        assert_equal(str_comp.longest_common_subseq(str0, str1), expected)
        print('Success: test_longest_common_subseq')


___ main(
    test = TestLongestCommonSubseq()
    test.test_longest_common_subseq()


__ __name__ __ '__main__':
    main()
