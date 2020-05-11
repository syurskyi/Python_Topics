_____ u__
_____ collections
from datetime _____ datetime, timedelta

from ..stock _____ Stock, StockSignal


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

    ___ test_price_is_the_latest_even_if_updates_are_made_out_of_order
        goog.update(datetime(2014, 2, 13), price=8)
        goog.update(datetime(2014, 2, 12), price=10)
        assertEqual(8, goog.price)


c_ StockTrendTest ?.?
    ___ given_a_series_of_prices goog, prices):
        timestamps = [datetime(2014, 2, 10), datetime(2014, 2, 11),
                      datetime(2014, 2, 12), datetime(2014, 2, 13)]
        for timestamp, price in zip(timestamps, prices):
            goog.update(timestamp, price)

    ___ test_stock_trends
        dataset = [
            ([8, 10, 12], True),
            ([8, 12, 10], False),
            ([8, 10, 10], False)
        ]
        for data in dataset:
            prices, output = data
            with subTest(prices=prices, output=output):
                goog = Stock("GOOG")
                given_a_series_of_prices(goog, prices)
                assertEqual(output, goog.is_increasing_trend())


c_ StockCrossOverSignalTest ?.?
    ___ setUp
        goog = Stock("GOOG")

    ___ _flatten timestamps):
        for timestamp in timestamps:
            if not isinstance(timestamp, collections.Iterable):
                yield timestamp
            else:
                for value in _flatten(timestamp):
                    yield value

    ___ _generate_timestamp_for_date date, price_list):
        if not isinstance(price_list, collections.Iterable):
            return date
        else:
            delta = 1.0/len(price_list)
            return [date + i*timedelta(delta) for i in range(len(price_list))]

    ___ _generate_timestamps price_list):
        return list(_flatten([
            _generate_timestamp_for_date(datetime(2014, 2, 13) -
                                              timedelta(i),
                                              price_list[len(price_list)-i-1])
            for i in range(len(price_list) - 1, -1, -1)
            if price_list[len(price_list) - i - 1] is not N..]))

    ___ given_a_series_of_prices price_list):
        timestamps = _generate_timestamps(price_list)
        for timestamp, price in zip(timestamps,
                                    list(_flatten([p
                                                        for p in price_list
                                                        if p is not N..]))):
            goog.update(timestamp, price)

    ___ test_generate_timestamp_returns_consecutive_dates
        price_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        expected = [
            datetime(2014, 2, 3), datetime(2014, 2, 4), datetime(2014, 2, 5),
            datetime(2014, 2, 6), datetime(2014, 2, 7), datetime(2014, 2, 8),
            datetime(2014, 2, 9), datetime(2014, 2, 10), datetime(2014, 2, 11),
            datetime(2014, 2, 12), datetime(2014, 2, 13)]
        assertEqual(expected, _generate_timestamps(price_list))

    ___ test_generate_timestamp_skips_empty_dates
        price_list = [1, 2, 3, N.., 5, 6, 7, 8, 9, 10, 11]
        expected = [
            datetime(2014, 2, 3), datetime(2014, 2, 4), datetime(2014, 2, 5),
            datetime(2014, 2, 7), datetime(2014, 2, 8),
            datetime(2014, 2, 9), datetime(2014, 2, 10), datetime(2014, 2, 11),
            datetime(2014, 2, 12), datetime(2014, 2, 13)]
        assertEqual(expected, _generate_timestamps(price_list))

    ___ test_generate_timestamp_handles_multiple_updates_per_date
        price_list = [1, 2, 3, [4, 3], 5, 6, 7, 8, 9, 10, 11]
        expected = [
            datetime(2014, 2, 3), datetime(2014, 2, 4), datetime(2014, 2, 5),
            datetime(2014, 2, 6), datetime(2014, 2, 6, 12),
            datetime(2014, 2, 7), datetime(2014, 2, 8),
            datetime(2014, 2, 9), datetime(2014, 2, 10), datetime(2014, 2, 11),
            datetime(2014, 2, 12), datetime(2014, 2, 13)]
        assertEqual(expected, _generate_timestamps(price_list))

    ___ test_stock_with_no_data_returns_neutral
        date_to_check = datetime(2014, 2, 13)
        given_a_series_of_prices([])
        assertEqual(StockSignal.neutral,
                         goog.get_crossover_signal(date_to_check))

    ___ test_stock_with_less_data_returns_neutral
        """Even though the series has a downward crossover, we return neutral
        because there are not enough data points"""
        date_to_check = datetime(2014, 2, 13)
        given_a_series_of_prices([
            20, 21, 22, 23, 24, 25, 26, 27, 28, 1])
        assertEqual(StockSignal.neutral,
                         goog.get_crossover_signal(date_to_check))

    ___ test_stock_with_no_crossover_returns_neutral
        date_to_check = datetime(2014, 2, 13)
        given_a_series_of_prices([
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
        assertEqual(StockSignal.neutral,
                         goog.get_crossover_signal(date_to_check))

    ___ test_with_downward_crossover_returns_sell
        date_to_check = datetime(2014, 2, 13)
        given_a_series_of_prices([
            21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 4])
        assertEqual(StockSignal.sell,
                         goog.get_crossover_signal(date_to_check))

    ___ test_with_upward_crossover_returns_buy
        date_to_check = datetime(2014, 2, 13)
        given_a_series_of_prices([
            29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 46])
        assertEqual(StockSignal.buy,
                         goog.get_crossover_signal(date_to_check))

    ___ test_should_only_look_at_closing_price
        date_to_check = datetime(2014, 2, 13)
        given_a_series_of_prices([
            29, [5, 28], [5, 27], 26, 25, 24, 23, 22, 21, 20, [5, 46]])
        assertEqual(StockSignal.buy,
                         goog.get_crossover_signal(date_to_check))

    ___ test_should_be_neutral_if_not_enough_days_of_data
        """Even though we have 13 updates, they only cover 10 days"""
        date_to_check = datetime(2014, 2, 13)
        given_a_series_of_prices([
            [5, 28], [5, 27], 26, 25, 24, 23, 22, 21, 20, [5, 46]])
        assertEqual(StockSignal.neutral,
                         goog.get_crossover_signal(date_to_check))

    ___ test_should_pick_up_previous_closing_if_no_updates_for_a_day
        date_to_check = datetime(2014, 2, 13)
        given_a_series_of_prices([
            29, 28, 27, 26, 25, 24, 23, 22, 21, 20, N.., N.., 46])
        assertEqual(StockSignal.buy,
                         goog.get_crossover_signal(date_to_check))

    ___ test_should_have_11_days_worth_of_data
        """Should return signal even if there is less than 11 number of updates
        as in the case where some days have no updates but we pick up the
        previous closing price to fill in the value"""
        date_to_check = datetime(2014, 2, 13)
        given_a_series_of_prices([
            27, 26, 25, 24, 23, 22, 21, 20, N.., N.., 46])
        assertEqual(StockSignal.buy,
                         goog.get_crossover_signal(date_to_check))

    ___ test_date_to_check_can_be_beyond_last_update_date
        """We have updates upto 13th, but we are checking signal on 15th.
        It should just fill in the values for 14th and 15th since there are
        no updates on these days"""
        date_to_check = datetime(2014, 2, 15)
        given_a_series_of_prices([
            29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 46])
        assertEqual(StockSignal.neutral,
                         goog.get_crossover_signal(date_to_check))
