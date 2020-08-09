from nose.tools ______ assert_equal
from nose.tools ______ assert_raises
from nose.tools ______ assert_true


class TestMaxProfit(object

    ___ test_max_profit(self
        stock_trader = StockTrader()
        assert_raises(TypeError, stock_trader.find_max_profit, None, None)
        assert_equal(stock_trader.find_max_profit(prices=[], k=0), [])
        prices = [5, 4, 3, 2, 1]
        k = 3
        assert_equal(stock_trader.find_max_profit(prices, k), (0, []))
        prices = [2, 5, 7, 1, 4, 3, 1, 3]
        profit, transactions = stock_trader.find_max_profit(prices, k)
        assert_equal(profit, 10)
        assert_true(Transaction(Type.SELL,
                                day=7,
                                price=3) in transactions)
        assert_true(Transaction(Type.BUY,
                                day=6,
                                price=1) in transactions)
        assert_true(Transaction(Type.SELL,
                                day=4,
                                price=4) in transactions)
        assert_true(Transaction(Type.BUY,
                                day=3,
                                price=1) in transactions)
        assert_true(Transaction(Type.SELL,
                                day=2,
                                price=7) in transactions)
        assert_true(Transaction(Type.BUY,
                                day=0,
                                price=2) in transactions)
        print('Success: test_max_profit')


___ main(
    test = TestMaxProfit()
    test.test_max_profit()


__ __name__ __ '__main__':
    main()