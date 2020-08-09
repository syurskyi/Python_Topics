from nose.tools ______ assert_equal, assert_raises


class TestCoinChange(object

    ___ test_coin_change(self
        coin_changer = CoinChanger()
        assert_raises(TypeError, coin_changer.make_change, None, None)
        assert_equal(coin_changer.make_change([], 0), 0)
        assert_equal(coin_changer.make_change([1, 2, 3], 5), 2)
        assert_equal(coin_changer.make_change([3, 2, 1], 5), 2)
        assert_equal(coin_changer.make_change([3, 2, 1], 8), 3)
        print('Success: test_coin_change')


___ main(
    test = TestCoinChange()
    test.test_coin_change()


__ __name__ __ '__main__':
    main()