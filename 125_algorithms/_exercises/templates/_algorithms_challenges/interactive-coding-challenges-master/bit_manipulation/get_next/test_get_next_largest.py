from nose.tools ______ assert_equal, assert_raises


class TestBits(object

    ___ test_get_next_largest(self
        bits = Bits()
        assert_raises(Exception, bits.get_next_largest, None)
        assert_raises(Exception, bits.get_next_largest, 0)
        assert_raises(Exception, bits.get_next_largest, -1)
        num = int('011010111', base=2)
        expected = int('011011011', base=2)
        assert_equal(bits.get_next_largest(num), expected)
        print('Success: test_get_next_largest')

    ___ test_get_next_smallest(self
        bits = Bits()
        assert_raises(Exception, bits.get_next_smallest, None)
        assert_raises(Exception, bits.get_next_smallest, 0)
        assert_raises(Exception, bits.get_next_smallest, -1)
        num = int('011010111', base=2)
        expected = int('011001111', base=2)
        assert_equal(bits.get_next_smallest(num), expected)
        print('Success: test_get_next_smallest')

___ main(
    test = TestBits()
    test.test_get_next_largest()
    test.test_get_next_smallest()


__ __name__ __ '__main__':
    main()