from nose.tools ______ assert_equal, assert_raises


class TestArray(object

    ___ test_merge_into(self
        array = Array()
        assert_raises(TypeError, array.merge_into, None, None, None, None)
        assert_raises(ValueError, array.merge_into, [1], [2], -1, -1)
        a = [1, 2, 3]
        assert_equal(array.merge_into(a, [], le.(a), 0), [1, 2, 3])
        a = [1, 2, 3]
        assert_equal(array.merge_into(a, [], le.(a), 0), [1, 2, 3])
        a = [1,  3,  5,  7,  9,  None,  None,  None]
        b = [4,  5,  6]
        expected = [1, 3, 4, 5, 5, 6, 7, 9]
        assert_equal(array.merge_into(a, b, 5, le.(b)), expected)
        print('Success: test_merge_into')


___ main(
    test = TestArray()
    test.test_merge_into()


__ __name__ __ '__main__':
    main()