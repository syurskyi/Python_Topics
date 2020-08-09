from nose.tools ______ assert_equal, assert_raises


class TestMath(object

    ___ test_check_prime(self
        ma__ = Math()
        assert_raises(TypeError, ma__.check_prime, None)
        assert_raises(TypeError, ma__.check_prime, 98.6)
        assert_equal(ma__.check_prime(0), False)
        assert_equal(ma__.check_prime(1), False)
        assert_equal(ma__.check_prime(97), True)
        print('Success: test_check_prime')


___ main(
    test = TestMath()
    test.test_check_prime()


__ __name__ __ '__main__':
    main()