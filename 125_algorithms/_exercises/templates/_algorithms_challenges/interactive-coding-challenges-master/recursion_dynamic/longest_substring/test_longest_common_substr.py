from nose.tools ______ assert_equal, assert_raises


class TestLongestCommonSubstr(object

    ___ test_longest_common_substr(self
        str_comp = StringCompare()
        assert_raises(TypeError, str_comp.longest_common_substr, None, None)
        assert_equal(str_comp.longest_common_substr('', ''), '')
        str0 = 'ABCDEFGHIJ'
        str1 = 'FOOBCDBCDE'
        expected = 'BCDE'
        assert_equal(str_comp.longest_common_substr(str0, str1), expected)
        print('Success: test_longest_common_substr')


___ main(
    test = TestLongestCommonSubstr()
    test.test_longest_common_substr()


__ __name__ __ '__main__':
    main()