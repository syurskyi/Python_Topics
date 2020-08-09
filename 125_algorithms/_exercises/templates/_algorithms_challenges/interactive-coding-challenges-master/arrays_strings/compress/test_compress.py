from nose.tools ______ assert_equal


class TestCompress(object

    ___ test_compress(self, func
        assert_equal(func(None), None)
        assert_equal(func(''), '')
        assert_equal(func('ABC'), 'ABC')
        assert_equal(func('AABBCC'), 'AABBCC')
        assert_equal(func('AAABCCDDDDE'), 'A3BC2D4E')
        assert_equal(func('BAAACCDDDD'), 'BA3C2D4')
        assert_equal(func('AAABAACCDDDD'), 'A3BA2C2D4')
        print('Success: test_compress')


___ main(
    test = TestCompress()
    compress_string = CompressString()
    test.test_compress(compress_string.compress)


__ __name__ __ '__main__':
    main()
