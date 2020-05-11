_____ u__
from datetime _____ datetime

from ..stock _____ Stock


c_ StockTest ?.?
    ___ setUp
        goog = Stock("GOOG")

    ___ test_price_of_a_new_stock_class_should_be_None
        aIN..(goog.price)

    ___ test_stock_update
        """An update should set the price on the stock object

        We will be  using the `datetime` module for the timestamp
        """
        goog.update(datetime(2014, 2, 12), price=10)
        assertEqual(10, goog.price)

    ___ test_negative_price_should_throw_ValueError
        with assertRaises(ValueError):
            goog.update(datetime(2014, 2, 13), -1)

    ___ test_stock_price_should_give_the_latest_price
        goog.update(datetime(2014, 2, 12), price=10)
        goog.update(datetime(2014, 2, 13), price=8.4)
        assertAlmostEqual(8.4, goog.price, delta=0.0001)


c_ StockTrendTest ?.?
    ___ setUp
        goog = Stock("GOOG")

    ___ given_a_series_of_prices prices):
        timestamps = [datetime(2014, 2, 10), datetime(2014, 2, 11),
                      datetime(2014, 2, 12), datetime(2014, 2, 13)]
        for timestamp, price in zip(timestamps, prices):
            goog.update(timestamp, price)

    ___ test_increasing_trend_is_true_if_price_increase_for_3_updates
        given_a_series_of_prices([8, 10, 12])
        assertTrue(goog.is_increasing_trend())

    ___ test_increasing_trend_is_false_if_price_decreases
        given_a_series_of_prices([8, 12, 10])
        assertFalse(goog.is_increasing_trend())

    ___ test_increasing_trend_is_false_if_price_equal
        given_a_series_of_prices([8, 10, 10])
        assertFalse(goog.is_increasing_trend())
